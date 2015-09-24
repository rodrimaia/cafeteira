from gpiocrust import Header, OutputPin, InputPin

class CoffeeMachine:
    RELAY_PIN = 13
    BUTTON_PIN = 15

    def __init__(self):
        self.header = Header()
        self.__relay = OutputPin(self.RELAY_PIN)
        self.__button = InputPin(self.BUTTON_PIN)

    def is_relay_on(self):
        return self.__relay.value

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
        GPIO.output(self.RELAY_PIN, activated)

    def register_button(self):
        GPIO.add_event_detect(self.BUTTON_PIN, GPIO.RISING, callback=self.buttonHandler, bouncetime=1200)
        print "Button registered"

    def buttonHandler(self, pin):
        global activated
        print "detectei botao"
        if(activated):
            self.stop()
        else:
            self.start()
