from gpiocrust import Header, OutputPin, InputPin
from logger import logger


class MachineAdapter:

    RELAY_PIN = 13
    BUTTON_PIN = 15
    activated = False

    def __init__(self):
        self.header = Header()
        self.__relay = OutputPin(self.RELAY_PIN)

    def is_relay_on(self):
        return self.__relay.value

    def start(self):
        self.__relay.value = True

    def stop(self):
        self.__relay.value = False

    def toggle(self):
        if(self.is_relay_on()):
            self.stop()
        else:
            self.start()

    def register_button(self, button_callback):
        if button_callback is None:
            button_callback = self.buttonHandler
        logger.debug('Button register')
        self.__buttonpin = InputPin(
            self.BUTTON_PIN, value=1, callback=button_callback,
            bouncetime=800)

    def buttonHandler(self):
        logger.debug('Button detected!')
        self.toggle()
