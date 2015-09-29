from gpiocrust import Header, OutputPin, InputPin

class CoffeeMachine:

    RELAY_PIN = 13
    BUTTON_PIN = 15
    activated = False

    def __init__(self):
        self.header = Header()
        self.__relaypin = OutputPin(self.RELAY_PIN)

    def get_state(self):
        global activated
        return activated

    def start(self):
        global activated
        activated = True
        self.change_state_pin()

    def stop(self):
        global activated
        activated = False
        self.change_state_pin()

    def change_state_pin(self):
        global activated
        self.__relaypin.value = activated

    def register_button(self):
        print "Button registered"
        self.__buttonpin = InputPin(self.BUTTON_PIN, callback=self.buttonHandler())

    def buttonHandler(self, pin):
        global activated
        print "detectei botao"
        if(activated):
            self.stop()
        else:
            self.start()
