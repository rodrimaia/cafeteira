import RPi.GPIO as GPIO

class CoffeeMachine:

    RELAY_PIN = 13
    BUTTON_PIN = 15
    state = None

    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.RELAY_PIN, GPIO.OUT)
        GPIO.setup(self.BUTTON_PIN, GPIO.IN)
        self.stop()

    def start(self):
        GPIO.output(self.RELAY_PIN, True)
        self.state = True

    def stop(self):
        GPIO.output(self.RELAY_PIN, False)
        self.state = False

    def register_button(self, action_button):
        GPIO.add_event_detect(self.BUTTON_PIN, GPIO.RISING, callback=action_button, bouncetime=1200)
        print "Button registered"
