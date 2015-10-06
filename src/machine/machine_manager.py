# -*- coding: utf-8 -*-
import time
from enum import Enum

from machine_adapter import MachineAdapter


class MachineStatus(Enum):
    stand_by = 1
    making_coffee = 2


class MachineManager:

    MAKE_COFFEE_TIME = 30

    def __init__(self):
        self.machine_adapter = MachineAdapter()
        self.machine_status = MachineStatus.stand_by

    def make_coffee(self):
        self.machine_adapter.start()
        self.machine_status = MachineStatus.making_coffee
        for _ in range(self.MAKE_COFFEE_TIME):
            self.wait_one_minute()

    def wait_one_minute(self):
        time.sleep(60)
