# -*- coding: utf-8 -*-

import datetime
from random import random
from twython import Twython

class TwitterWrapper(Twython):
    def __init__(self):
        APP_KEY = 'APK6SDMtvi6POlzcFYxiV0idB'
        APP_SECRET = 'tY9KKokGH2OjQVckPK6ouKhRy3ET5uKsuiazO2eZH0ecZK9v3i'
        ACCESS_TOKEN = '3496812391-DBNN5rAROcur5UykIQY5nCTNMoTNSTopG4kLVN1'
        ACCESS_SECRET = 'iWvF7JkaN4OWw40RmCMTQMzol4JsoMSyptKZecIAxZRAO'
        super(TwitterWrapper, self).__init__(APP_KEY, APP_SECRET, ACCESS_TOKEN,ACCESS_SECRET)

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

