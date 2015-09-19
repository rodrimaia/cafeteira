import time
import schedule

from machine import CoffeeMachine
from twitter import TwitterWrapper

class CoffeeJob:

    def __init__(self):
        self.state = None

    def start(self):
        print "Starting the CoffeeJob... "
        self.cm = CoffeeMachine()
        self.cm.register_button(self.stop_callback)
        self.state = True

        while self.state:
            print self.cm.state
            time.sleep(1)

    def stop(self):
        print "Stopping the CoffeeJob... "
        self.state = False

    def stop_callback(self):
        print "PANIC BUTTON PRESSED!"
        self.cm.stop()
