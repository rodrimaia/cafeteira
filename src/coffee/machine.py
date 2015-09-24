from gpiocrust import Header, OutputPin, InputPin

class CoffeeMachine:

    RELAY_PIN = 13
    BUTTON_PIN = 15
    activated = False

    def __init__(self):
<<<<<<< HEAD
        self.header = Header()
        self.relay = OutputPin(self.RELAY_PIN)
        self.button = InputPin(self.BUTTON_PIN)
=======
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.RELAY_PIN, GPIO.OUT)
        GPIO.setup(self.BUTTON_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)
>>>>>>> cria status para verificar calendario

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
        GPIO.output(self.RELAY_PIN, activated)

    def register_button(self):
        GPIO.add_event_detect(self.BUTTON_PIN, GPIO.RISING, callback=self.buttonHandler, bouncetime=1200)
        print "Button registered"

    def buttonHandler(pin):
        global activated
        print "detectei " + str(activated)
        if(activated):
            self.stop()
        else:
            self.start()