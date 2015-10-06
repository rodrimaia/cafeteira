# -*- coding: utf-8 -*-
import time
from enum import Enum

from machine_adapter import MachineAdapter


class MachineStatus(Enum):
    stand_by = 1
    making_coffee = 2
    warming_coffee = 3


class MachineManager:

    MAKE_COFFEE_TIME = 30
    WARM_COFFEE_TIME = 30

    def __init__(self):
        self.machine_adapter = MachineAdapter()
        self.machine_status = MachineStatus.stand_by

    def make_coffee(self):
        print 'comecando a fazer cafe'
        self.machine_adapter.start()
        self.machine_status = MachineStatus.making_coffee
        for _ in range(self.MAKE_COFFEE_TIME):
            self.wait_one_minute()

    def keep_coffee_hot(self):
        print 'esquentando cafe'
        self.machine_status = MachineStatus.warming_coffee
        for _ in range(self.WARM_COFFEE_TIME):
            self.machine_adapter.stop()
            self.wait_one_minute()
            self.machine_adapter.start()
            self.wait_one_minute()

    def wait_one_minute(self):
        time.sleep(60)
