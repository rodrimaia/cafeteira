import time
import schedule

from machine import CoffeeMachine
from twitter.twitter import CoffeeTwitter

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
        self.make_coffee()
        self.keep_coffee_hot()

    def make_coffee(self):
        print "Start make coffee"
        self.twitter.tweet()
        self.cm.start()
        count = 0
        while self.cm.state or count < (60*INTERVAL):
            time.sleep(1)
            count+=1
        keep_coffee_hot()


    def keep_coffee_hot(self):
        print "Keeping coffe hot"
        for i in range(0, self.INTERVAL):
            time.sleep(60)
            self.cm.start()
            time.sleep(60)
            self.cm.stop()

    def stop(self):
        print "Stopping the CoffeeJob... "
        self.cm.state = False
        self.cm.stop()

    def stop_callback(self, pin):
        print "PANIC BUTTON PRESSED!"
        if(self.cm.state):
            print "Stoping button"
            self.twitter.tweet_panic()
            self.stop()
        else:
            print "Starting button"
            self.start()
