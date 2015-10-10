import unittest

from machine.machine_manager import MachineManager, MachineStatus
from mock import MagicMock, Mock


class MachineManagerTest(unittest.TestCase):

    def setUp(self):
        self.target = MachineManager()
        self.adapter_start_mock = MagicMock()
        self.adapter_stop_mock = MagicMock()
        self.target.machine_adapter.start = self.adapter_start_mock
        self.target.machine_adapter.stop = self.adapter_stop_mock
        MachineManager.wait_one_minute = MagicMock()

    def test_machine_routine_should_make_and_keep_coffee_hot(self):
        self.target.make_coffee = Mock(wraps=self.target.make_coffee)
        self.target.keep_coffee_hot = Mock(wraps=self.target.keep_coffee_hot)
        interrupt_mock = Mock(wraps=self.target.interrupt_machine)
        self.target.interrupt_machine = interrupt_mock

        self.target.start_coffee_routine()

        self.assertTrue(self.target.make_coffee.called)
        self.assertTrue(self.target.keep_coffee_hot.called)
        self.assertTrue(self.target.interrupt_machine.called)

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

    def test_machine_should_set_machine_standby_when_making_coffee(self):
        self.target.machine_status = MachineStatus.making_coffee
        self.target.go_back_stand_by()
        self.assertEquals(self.target.machine_status, MachineStatus.stand_by)
        self.assertEquals(self.adapter_stop_mock.call_count, 1)

    def test_machine_should_set_machine_standby_when_warming_coffee(self):
        self.target.machine_status = MachineStatus.warming_coffee
        self.target.go_back_stand_by()
        self.assertEquals(self.target.machine_status, MachineStatus.stand_by)
        self.assertEquals(self.adapter_stop_mock.call_count, 1)

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
        make_coffee_mock = Mock(wraps=self.target.make_coffee)
        keep_coffee_hot = Mock(wraps=self.target.keep_coffee_hot)
        go_back_stand_by = Mock(wraps=self.target.go_back_stand_by)
        self.target.make_coffee = make_coffee_mock
        self.target.keep_coffee_hot = keep_coffee_hot
        self.target.go_back_stand_by = go_back_stand_by
        self.target.interrupt_machine()
        self.assertTrue(self.target.make_coffee.called)
        self.assertTrue(self.target.keep_coffee_hot.called)
        self.assertTrue(self.target.go_back_stand_by.called)
