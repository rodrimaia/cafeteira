# from datetime import datetime
# from twython import Twython
# from messages import MessagesTwitter
# from credentials import keys

# APP_KEY = keys['APP_KEY']
# APP_SECRET = keys['APP_SECRET']
# ACCESS_TOKEN = keys['ACCESS_TOKEN']
# ACCESS_SECRET = keys['ACCESS_SECRET']


# class TwitterWrapper(Twython):

#     def __init__(self):
#         super(TwitterWrapper, self).__init__(
#             APP_KEY, APP_SECRET, ACCESS_TOKEN, ACCESS_SECRET)


# class CoffeeTwitter(object):
#     # ativa twitter
#     TWITTER_ACTIVE = True

#     def __init__(self):
#         if self.TWITTER_ACTIVE:
#             self.twitter = TwitterWrapper()
#             self.messages = MessagesTwitter()

#     def tweet(self):
#         if self.TWITTER_ACTIVE:
#             now = datetime.now()
#             status = self.messages.get_message_making_coffee()
#             self.twitter.update_status(status=status %
#                (now.hour, now.minute))

#     def tweet_panic(self):
#         if self.TWITTER_ACTIVE:
#             now = datetime.now()
#             status = self.messages.get_message_abort()
#             self.twitter.update_status(status=status %
#                (now.hour, now.minute))
