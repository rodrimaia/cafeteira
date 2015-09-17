from unittest import TestCase, main
from mock import patch, call

from coffeemachine import CoffeeMachine

import pdb

class CoffeeMachineTest(TestCase):

    def test_start(self):
        cm = CoffeeMachine()
        cm.start()
        assert cm.relay.value

    def test_stop(self):
        cm = CoffeeMachine()
        cm.stop()
        assert cm.relay.value == False


if __name__ == "__main__":
    main()
