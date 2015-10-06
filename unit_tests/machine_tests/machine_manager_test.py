import unittest

from machine.machine_manager import MachineManager, MachineStatus
from mock import MagicMock


class MachineManagerTest(unittest.TestCase):

    def setUp(self):
        self.target = MachineManager()
        self.adapter_mock = MagicMock()
        self.target.machine_adapter.start = self.adapter_mock
        MachineManager.wait_one_minute = MagicMock()

    def test_machine_should_make_coffee(self):
        self.target.make_coffee()
        self.assertEquals(self.target.machine_status,
                          MachineStatus.making_coffee)
        self.assertTrue(self.adapter_mock.called)
        self.assertEquals(MachineManager.wait_one_minute.call_count, 30)
