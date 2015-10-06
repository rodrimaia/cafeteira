import unittest
from machine.machine_adapter import MachineAdapter


class MachineTest(unittest.TestCase):

    def setUp(self):
        self.machine = MachineAdapter()

    def test_machine_relay_should_start_turned_off(self):
        self.assertFalse(self.machine.is_relay_on())

    def test_start_should_turn_relay_on(self):
        self.machine.start()
        self.assertTrue(self.machine.is_relay_on())

    def test_stop_should_turn_relay_off(self):
        self.machine.stop()
        self.assertFalse(self.machine.is_relay_on())

    def test_toggle_should_alternate_relay_values(self):
        self.machine.toggle()
        self.assertTrue(self.machine.is_relay_on())
        self.machine.toggle()
        self.assertFalse(self.machine.is_relay_on())

    def test_button_toggle_machine(self):
        self.machine.buttonHandler()
        self.assertTrue(self.machine.is_relay_on())

    def test_button_toggle_machine_stopped(self):
        self.machine.start()
        self.machine.buttonHandler()
        self.assertFalse(self.machine.is_relay_on())
