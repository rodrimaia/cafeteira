import time

from schedule.schedule_manager import ScheduleManager
from machine.machine_manager import MachineManager, MachineStatus
from schedule.schedule_reader import ScheduleReader
from threading import Thread
from api.api_manager import ApiManager
from logger import logger


current_action = None


class Cafeteira:

    def __init__(self):
        self.scheduled_times = self.setup_schedule()
        self.schedule = ScheduleManager(self.scheduled_times)
        self.machine = MachineManager()
        self.machine.listen_button(self.button_callback)
        self.start_schedule_process()
        self.start_api_process()

    def get_machine_status(self):
        return self.machine.machine_status

    def get_schedule_times(self):
        return self.scheduled_times

    def button_callback(self, pin):
        logger.debug('Button panic activaded!')
        if (self.machine.machine_status is MachineStatus.stand_by):
            self.start_coffee_routine_async()
        else:
            self.machine.go_back_stand_by()

    def setup_schedule(self):
        FILE_PATH = 'schedule_coffee.txt'
        reader = ScheduleReader(FILE_PATH)
        times = reader.read_scheduled_times()
        return times

    def check_schedule_are_ok(self):
        while (True):
            if (self.schedule.its_time() and
                    self.machine.machine_status is MachineStatus.stand_by):
                logger.debug('Schedule time is Ok!')
                self.start_coffee_routine_async()
            time.sleep(30)

    def start_api_process(self):
        logger.debug('Create process for API')
        self.api = ApiManager(self)
        self.api.start()
        thread_api = Thread(target=self.api.start)
        thread_api.start()

    def start_schedule_process(self):
        logger.debug('Create process for Schedule Reader')
        thread_reading_schedule = Thread(target=self.check_schedule_are_ok)
        thread_reading_schedule.start()

    def start_coffee_routine_async(self):
        if (self.machine.machine_status is MachineStatus.stand_by):
            logger.debug('Create thread for coffee')
            thread_making_coffee = Thread(
                target=self.machine.start_coffee_routine
            )
            thread_making_coffee.start()
