import time
import schedule

from machine import CoffeeMachine
from twitter.twitter import CoffeeTwitter
from datetime import datetime

class CoffeeJob:
    TIMER = 15
    INTERVAL = 30

    state = None

    def __init__(self):
        self.twitter = CoffeeTwitter()
        self.cm = CoffeeMachine()
        self.cm.stop()
        self.cm.register_button(self.stop_callback)
        self.state = True
     
    def start(self):
        while self.state:
            print "verifica calendario"
            print self.read_schedule()
            if self.read_schedule():
                print "Starting the CoffeeJob... "
                self.make_coffee()
            time.sleep(50)
        
    def make_coffee(self):
        print "Start make coffee"
        self.twitter.tweet()
        self.cm.start()
        count = 0
        while count < (60*self.INTERVAL):
            time.sleep(1)
            count+=1
        self.keep_coffee_hot()
        self.state = True

    
    def read_schedule(self):
        now = datetime.now()
        lines = [line.rstrip() for line in open("schedule_coffee.txt")]
        time_temp = "%02d:%02d" % (now.hour, now.minute)
        return time_temp in lines

    def keep_coffee_hot(self):
        print "Keeping coffe hot"
        if self.cm.state:
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
            print "Starting make coffe again"
            self.state = False
            self.make_coffee()
