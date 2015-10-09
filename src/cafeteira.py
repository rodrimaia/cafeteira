import time

from machine.machine_manager import MachineManager, MachineStatus
from schedule.schedule_manager import ScheduleManager
from schedule.schedule_reader import ScheduleReader
from api.api import Api


class Cafeteira:

    def __init__(self):
        self.schedule = self.setup_schedule()
        self.machine = MachineManager()
        self.machine.listen_button(self.button_callback)
        Api(self.machine).start()
        print 'comecando a esperar'

        while(True):
            if (self.schedule.its_time() and
                    self.machine.machine_status == MachineStatus.stand_by):
                print 'horario confere com agendado'
                self.machine.make_coffee()
                self.machine.keep_coffee_hot()
                self.machine.go_back_stand_by()
            time.sleep(59)

    def button_callback(self, pin):
        print "botao acionado"
        if (self.machine.machine_status == MachineStatus.stand_by):
            self.machine.make_coffee()
            self.machine.keep_coffee_hot()
            self.machine.go_back_stand_by()
        else:
            self.machine.interrupt()

    def setup_schedule(self):
        FILE_PATH = 'schedule_coffee.txt'
        reader = ScheduleReader(FILE_PATH)
        times = reader.read_scheduled_times()
        return ScheduleManager(times)
