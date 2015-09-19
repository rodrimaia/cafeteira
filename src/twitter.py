from twython import Twython

class TwitterWrapper(Twython):
    def __init__(self):
        APP_KEY = 'APK6SDMtvi6POlzcFYxiV0idB'
        APP_SECRET = 'tY9KKokGH2OjQVckPK6ouKhRy3ET5uKsuiazO2eZH0ecZK9v3i'
        ACCESS_TOKEN = '3496812391-DBNN5rAROcur5UykIQY5nCTNMoTNSTopG4kLVN1'
        ACCESS_SECRET = 'iWvF7JkaN4OWw40RmCMTQMzol4JsoMSyptKZecIAxZRAO'
        super(TwitterWrapper, self).__init__(APP_KEY, APP_SECRET, ACCESS_TOKEN,ACCESS_SECRET)

