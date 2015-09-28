# -*- coding: utf-8 -*-

from twython import TwythonStreamer
from credentials import keys

APP_KEY = keys['APP_KEY']
APP_SECRET = keys['APP_SECRET']
ACCESS_TOKEN = keys['ACCESS_TOKEN']
ACCESS_SECRET = keys['ACCESS_SECRET']

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            print data['text'].encode('utf-8')

    def on_error(self, status_code, data):
        print status_code


stream = MyStreamer(APP_KEY, APP_SECRET,ACCESS_TOKEN, ACCESS_SECRET)
stream.statuses.filter(track='#CBSOFTTest2015')
