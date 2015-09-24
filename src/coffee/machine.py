from gpiocrust import Header, OutputPin, InputPin

class CoffeeMachine:

    RELAY_PIN = 13
    BUTTON_PIN = 15
    state = None

    def __init__(self):
        self.header = Header()
        self.relay = OutputPin(self.RELAY_PIN)
        self.button = InputPin(self.BUTTON_PIN)

    def start(self):
        self.state = True
        self.change_state_pin()

    def stop(self):
        self.state = False
        self.change_state_pin()

    def change_state_pin(self):
        GPIO.output(self.RELAY_PIN, self.state)

    def register_button(self, action_button):
        GPIO.add_event_detect(self.BUTTON_PIN, GPIO.RISING, callback=action_button, bouncetime=1200)
        print "Button registered"
