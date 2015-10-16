import time

from machine.machine_manager import MachineManager, MachineStatus
from schedule.schedule_manager import ScheduleManager
from schedule.schedule_reader import ScheduleReader
from multiprocessing import Process
from api.api_manager import ApiManager


current_action = None


class Cafeteira:

    def __init__(self):
        self.schedule = self.setup_schedule()
        self.machine = MachineManager()
        self.machine.listen_button(self.button_callback)
        self.start_api_process()
        self.start_schedule_process()

    def get_machine_status(self):
        return self.machine.machine_status

    def button_callback(self, pin):
        print "botao acionado"
        if (self.machine.machine_status == MachineStatus.stand_by):
            self.machine.start_coffee_routine()
        else:
            self.machine.interrupt()

    def setup_schedule(self):
        FILE_PATH = 'schedule_coffee.txt'
        reader = ScheduleReader(FILE_PATH)
        times = reader.read_scheduled_times()
        return ScheduleManager(times)

    def check_schedule_are_ok(self):
        global current_action
        while (True):
            if (self.schedule.its_time() and current_action is None):
                print 'Schedule time is ok'
                self.start_coffee_routine_async()
            time.sleep(30)

    def start_api_process(self):
        self.api = ApiManager(self)
        self.api.start()
        thread_api = Process(target=self.api.start)
        thread_api.start()

    def start_schedule_process(self):
        thread_reading_schedule = Process(target=self.check_schedule_are_ok)
        thread_reading_schedule.start()

    def start_coffee_routine_async(self):
        global current_action
        if current_action is None:
            print "Create thread for coffee"
            thread_making_coffee = Process(
                target=self.machine.start_coffee_routine)
            thread_making_coffee.start()
            current_action = thread_making_coffee
