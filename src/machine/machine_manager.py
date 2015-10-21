# -*- coding: utf-8 -*-
from enum import Enum
from datetime import datetime
from machine_adapter import MachineAdapter
from logger import logger


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

    def start_coffee_routine(self):
        self.make_coffee()
        self.keep_coffee_hot()
        self.go_back_stand_by()

    def make_coffee(self):
        logger.debug('Start make coffee')
        self.machine_adapter.start()
        self.machine_status = MachineStatus.making_coffee
        for _ in range(self.MAKE_COFFEE_TIME):
            self.wait_one_minute()

    def keep_coffee_hot(self):
        logger.debug('Keep coffee hot for 60 minuts')
        self.machine_status = MachineStatus.warming_coffee
        for _ in range(self.WARM_COFFEE_TIME):
            self.machine_adapter.stop()
            self.wait_one_minute()
            self.machine_adapter.start()
            self.wait_one_minute()

    def go_back_stand_by(self):
        logger.debug('Send coffee machine to stand by mod')
        self.machine_status = MachineStatus.stand_by
        self.machine_adapter.stop()

    def interrupt_machine(self):
        if(self.machine_status != MachineStatus.stand_by):
            self.go_back_stand_by()
        else:
            self.start_coffee_routine()

    def listen_button(self, button_callback):
        logger.debug('Listen button')
        self.machine_adapter.register_button(button_callback)

    def wait_one_minute(self):
        target = datetime.now()
        while(target.minute == datetime.now().minute):
            pass
