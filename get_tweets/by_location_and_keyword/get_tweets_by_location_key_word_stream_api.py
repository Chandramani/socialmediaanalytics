from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from keys import keys
import time
import json

# Variables that contains the user credentials to access Twitter API
consumer_key = keys['consumer_key']
consumer_secret = keys['consumer_secret']
access_token = keys['access_token']
access_token_secret = keys['access_token_secret']


# This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):
    track_words = ['bc subplan', 'bc sub plan', 'bc reservations', 'bc reservation', 'bc sub-plan', 'obc subplan',
                   'obc sub plan',
                   'obc sub-plan', 'obc reservations', 'obc reservation', 'caste reservation', '#SingleBecause',
                   '#SuperstarKidnap', 'bc']
    # make this config driven

    def on_data(self, data):
        try:
            saveFile = open('location_keyword_tweets.json', 'a')
            data = json.loads(data)
            # print data["text"]
            if any(x in data["text"] for x in self.track_words):
                print data["text"]
                saveFile.write(data)
                saveFile.close()
                # return True
            else:
                pass  # print "no match"

        except BaseException, e:
            print 'failed on data,', str(e), data["text"]
            time.sleep(5)
            pass

    def on_error(self, status):
        print status


if __name__ == '__main__':
    # This handles Twitter authentication and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    hyderabad_geo_box = [78.2176, 17.18278, 78.693248, 17.624824]
    stream.filter(locations=hyderabad_geo_box)