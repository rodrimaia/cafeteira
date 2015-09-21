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
        self.cm = CoffeeMachine()
        self.cm.register_button(self.stop_callback)

    def start(self):
        print "Starting the CoffeeJob... "
        self.state = True

        self.twitter.tweet()
        self.cm.start()
        time.sleep(60*self.TIMER)
        self.stop()

        for i in range(0, self.INTERVAL):
            self.cm.start()
            time.sleep(60)
            self.cm.stop()

    def stop(self):
        print "Stopping the CoffeeJob... "
        self.state = False

    def stop_callback(self, pin):
        print "PANIC BUTTON PRESSED!"
        if(self.cm.state):
            print "Stoping"
            self.twitter.tweet_panic()
            self.stop()
        else:
            print "Starting"
            self.start()
