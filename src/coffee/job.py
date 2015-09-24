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
        self.state = False
     
    def start(self):
        while True:
            print "verifica calendario"
            print self.read_schedule()
            if self.read_schedule() or self.state:
                print "Starting the CoffeeJob... "
                self.make_coffee()
            time.sleep(50)
        
    def make_coffee(self):
        print "Start make coffee"
        #self.twitter.tweet()
        self.cm.start()
        time.sleep(60*self.INTERVAL)       
        self.keep_coffee_hot()
        self.state = False
    
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
                self.cm.stop()
                time.sleep(60)
                self.cm.start()

    def stop(self):
        print "Stopping the CoffeeJob... "
        self.state = False
        self.cm.stop()

    def stop_callback(self, pin):
        print "PANIC BUTTON PRESSED!"
        if(self.cm.state):
            print "Stoping button"
            #self.twitter.tweet_panic()
            self.stop()
        else:
            print "Starting make coffe again"
            self.state = True
            self.start()
