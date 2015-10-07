import unittest

from machine.machine_manager import MachineManager, MachineStatus
from mock import MagicMock


class MachineManagerTest(unittest.TestCase):

    def setUp(self):
        self.target = MachineManager()
        self.adapter_start_mock = MagicMock()
        self.adapter_stop_mock = MagicMock()
        self.target.machine_adapter.start = self.adapter_start_mock
        self.target.machine_adapter.stop = self.adapter_stop_mock
        MachineManager.wait_one_minute = MagicMock()

    def test_machine_should_make_coffee(self):
        self.target.make_coffee()
        self.assertEquals(self.target.machine_status,
                          MachineStatus.making_coffee)
        self.assertTrue(self.adapter_start_mock.called)
        self.assertEquals(MachineManager.wait_one_minute.call_count, 30)

    def test_machine_should_keep_coffee_hot(self):
        self.target.keep_coffee_hot()
        self.assertEquals(self.target.machine_status,
                          MachineStatus.warming_coffee)
        self.assertEquals(self.adapter_stop_mock.call_count, 30)
        self.assertEquals(self.adapter_start_mock.call_count, 30)
        self.assertEquals(MachineManager.wait_one_minute.call_count, 60)

    def test_machine_interrupt_should_stop_making_coffee(self):
        self.target.make_coffee()
        self.target.interrupt_machine()
        self.assertEquals(self.target.machine_status, MachineStatus.stand_by)
        self.assertTrue(self.adapter_stop_mock.called)

    def test_machine_interrupt_should_stop_keeping_coffee_hot(self):
        self.target.keep_coffee_hot()
        self.target.interrupt_machine()
        self.assertEquals(self.target.machine_status, MachineStatus.stand_by)
        self.assertTrue(self.adapter_stop_mock.called)

    def test_machine_interrupt_should_start_machine_if_it_is_in_stand_by(self):
        self.target.interrupt_machine()
        status = self.target.machine_status
        self.assertEquals(status, MachineStatus.making_coffee)
        self.assertTrue(self.adapter_start_mock.called)
