from twython import TwythonStreamer


class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            print data['text'].encode('utf-8')

    def on_error(self, status_code, data):
        print status_code



APP_KEY = 'APK6SDMtvi6POlzcFYxiV0idB'
APP_SECRET = 'tY9KKokGH2OjQVckPK6ouKhRy3ET5uKsuiazO2eZH0ecZK9v3i'
ACCESS_TOKEN = '3496812391-DBNN5rAROcur5UykIQY5nCTNMoTNSTopG4kLVN1'
ACCESS_SECRET = 'iWvF7JkaN4OWw40RmCMTQMzol4JsoMSyptKZecIAxZRAO'

stream = MyStreamer(APP_KEY, APP_SECRET,
                            ACCESS_TOKEN, ACCESS_SECRET)
stream.statuses.filter(track='#CBSOFTTest2015')
