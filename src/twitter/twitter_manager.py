import twitter_messages as messages


from logger import logger
from datetime import datetime
from twython import Twython
from twitter_credentials import keys

APP_KEY = keys['APP_KEY']
APP_SECRET = keys['APP_SECRET']
ACCESS_TOKEN = keys['ACCESS_TOKEN']
ACCESS_SECRET = keys['ACCESS_SECRET']


class TwitterWrapper(Twython):

    def __init__(self):
        super(TwitterWrapper, self).__init__(
            APP_KEY, APP_SECRET, ACCESS_TOKEN, ACCESS_SECRET)


class TwitterManager(object):

    def update_status(self, message):
        twitter = TwitterWrapper()
        logger.debug('called post message')
        logger.debug(message)
        twitter.update_status(
            status=message
        )

    def transform_message(self, message):
        now = datetime.now()
        return message % (now.hour, now.minute)

    def tweet_turn_on_machine(self):
        logger.debug('call tweet turn on machine')
        self.update_status(
            self.transform_message(messages.msg_making)
        )

    def tweet_turn_off_machine(self):
        logger.debug('call tweet turn off machine')
        self.update_status(
            self.transform_message(messages.msg_abort)
        )
