# -*- coding: utf-8 -*-

from datetime import datetime
from random import random
from twython import Twython
import credentials

class TwitterWrapper(Twython):
    def __init__(self):
        super(TwitterWrapper, self).__init__(credentials.APP_KEY, credentials.APP_SECRET, credentials.ACCESS_TOKEN,ACCESS_SECRET)

class CoffeeTwitter(object):
    
    def __init__(self):
        self.twitter = TwitterWrapper()

    def tweet(self):
        now = datetime.now()
        status = self.get_status()
        self.twitter.update_status(status = status % (now.hour, now.minute))

    def get_status(self):
        TWEETS = [
            "Olá, agora são %d hora(s) e %d minuto(s), o que acha de tomar um café? ThoughtWorks @ #CBSOFT2015",
            "%02d:%02d começando os preparativos para um café. ThoughtWorks @ #CBSOFT2015"
        ]

        return TWEETS[int(random()*len(TWEETS))]

    def tweet_panic(self):
        now = datetime.now()
        status = self.get_status_panic()
        self.twitter.update_status(status = status % (now.hour, now.minute))

    def get_status_panic(self):
        return "Olá, agora são %d hora(s) e %d minuto(s), deu treta na cafeteira, voltamos em alguns minutos!"
