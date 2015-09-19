from unittest import TestCase, main
from machine import CoffeeMachine

class CoffeeMachineTests(TestCase):

    def test_start(self):
        cm = CoffeeMachine()
        cm.start()
        self.assertTrue(cm.relay.value)

    def test_stop(self):
        cm = CoffeeMachine()
        cm.stop()
        self.assertFalse(cm.relay.value)


if __name__ == "__main__":
    main()
