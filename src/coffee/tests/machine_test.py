import unittest
from ..machine import CoffeeMachine

class MachineTest(unittest.TestCase):
    
    def setUp(self):
        self.machine = CoffeeMachine()

    def test_machine_rele_should_start_turned_off(self):
        assert self.machine.relay.value == False
