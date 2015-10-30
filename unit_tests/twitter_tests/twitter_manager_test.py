# -*- coding: utf-8 -*-
import unittest


from twitter.twitter_manager import TwitterManager
from mock import MagicMock
from freezegun import freeze_time


class TwitterManagerTest(unittest.TestCase):

    def setUp(self):
        self.target = TwitterManager()
        self.target.update_status = MagicMock()

    def test_twitter_turn_on_machine(self):
        self.target.transform_message = MagicMock()
        self.target.tweet_turn_on_machine()
        self.assertTrue(self.target.update_status.called)
        self.assertTrue(self.target.transform_message.called)

    def test_twitter_turn_off_machine(self):
        self.target.transform_message = MagicMock()
        self.target.tweet_turn_off_machine()
        self.assertTrue(self.target.update_status.called)
        self.assertTrue(self.target.transform_message.called)

    @freeze_time("2015-10-10 10:00:00")
    def test_twitter_message_transform(self):
        message = self.target.transform_message("%02d:%02d teste!!")
        self.assertEquals('10:00 teste!!', message)
