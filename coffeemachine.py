import RPi.GPIO as GPIO

class CoffeeMachine:
    relayPin = 13

    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.relayPin, GPIO.OUT)

    def start(self):
        GPIO.output(self.relayPin, True)

    def stop(self):
        GPIO.output(self.relayPin, False)


