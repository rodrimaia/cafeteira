import time
import schedule

from machine import CoffeeMachine
from twitter import CoffeeTwitter

class CoffeeJob:
    TIMER = 15
    INTERVAL = 30

    def __init__(self):
        self.state = None
        self.twitter = CoffeeTwitter()

    def start(self):
        print "Starting the CoffeeJob... "
        self.cm = CoffeeMachine()
        self.cm.register_button(self.stop_callback)
        self.state = True

        while self.state:
            print self.cm.state
            time.sleep(1)
            self.twitter.tweet()
            self.cm.start()
            time.sleep(60*self.TIMER)
            self.cm.stop()
            time.sleep(60*self.INTERVAL)

    def stop(self):
        print "Stopping the CoffeeJob... "
        self.state = False

    def stop_callback(self, pin):
        print "Stoping"
        print "PANIC BUTTON PRESSED!"
        self.cm.stop()
