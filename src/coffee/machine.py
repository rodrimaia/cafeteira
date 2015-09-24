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
        self.__relay.value = True

    def stop(self):
        self.__relay.value = False

    def toggle(self):
        if(self.is_relay_on()):
            self.stop()
        else:
            self.start()

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
