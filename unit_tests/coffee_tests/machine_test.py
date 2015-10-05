import unittest
from coffee.machine import CoffeeMachine

class MachineTest(unittest.TestCase):

    def setUp(self):
        self.machine = CoffeeMachine()

    def test_machine_relay_should_start_turned_off(self):
        assert self.machine.is_relay_on() == False

    def test_start_should_turn_relay_on(self):
        self.machine.start()
        assert self.machine.is_relay_on() == True

    def test_stop_should_turn_relay_off(self):
        self.machine.stop()
        assert self.machine.is_relay_on() == False

    def test_toggle_should_alternate_relay_values(self):
        self.machine.toggle()
        assert self.machine.is_relay_on() == True
        self.machine.toggle()
        assert self.machine.is_relay_on() == False

    def test_button_toggle_machine(self):
        self.machine.buttonHandler()
        assert self.machine.is_relay_on() == True

    def test_button_toggle_machine_stopped(self):
        self.machine.start()
        self.machine.buttonHandler()
        self.assertEqual(self.machine.is_relay_on(),False)
