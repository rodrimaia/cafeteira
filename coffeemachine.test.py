from unittest import TestCase, main
from mock import patch, call

from RPi.GPIO import BOARD, OUT
from coffeemachine import CoffeeMachine

import pdb

@patch("RPi.GPIO.setup")
@patch("RPi.GPIO.setmode")
class CoffeeMachineTest(TestCase):
    
    def test_init_with_setmode(self, setmode, *args, **kwargs):
        cm = CoffeeMachine()
        setmode.assert_called_with(BOARD)
    
    def test_init_with_setup(self, setmode, setup, *args, **kwargs):
        cm = CoffeeMachine()
        setup.assert_called_with(cm.relayPin, OUT)

    @patch("RPi.GPIO.output")
    def test_start(self, output, *args, **kwargs):
        cm = CoffeeMachine()
        cm.start()
        output.assert_called_with(cm.relayPin, True)

    @patch("RPi.GPIO.output")
    def test_stop(self, output, *args, **kwargs):
        cm = CoffeeMachine()
        cm.stop()
        output.assert_called_with(cm.relayPin, False)


if __name__ == "__main__":
    main()
