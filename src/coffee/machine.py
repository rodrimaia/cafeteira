from gpiocrust import  Header, OutputPin, InputPin

class CoffeeMachine:

    RELAY_PIN = 13
    BUTTON_PIN = 15
    state = None

    def __init__(self):
	self.header = Header()
        self.relay = OutputPin(self.RELAY_PIN)
        self.stop()

    def start(self):
        self.relay.value = True
        self.state = True

    def stop(self):
        self.relay.value = False
        self.state = False

    def register_button(self, callback):
        self.button = InputPin(self.BUTTON_PIN, callback=callback, bouncetime=1200)
        print "Button registered"
