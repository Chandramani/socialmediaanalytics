
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from keys import keys
import time

# make sure the keys used in this application is not used by any other application

# Variables that contains the user credentials to access Twitter API
consumer_key = keys['consumer_key']
consumer_secret = keys['consumer_secret']
access_token = keys['access_token']
access_token_secret = keys['access_token_secret']


# This is a basic listener, writes tweets to data file.
class StdOutListener(StreamListener):

    def on_data(self, data):
                        try:

                                save_file = open('raw_tweets_by_location.json', 'a')
                                print data
                                save_file.write(data)
                                save_file.close()
                                return True

                        except BaseException, e:
                                print 'failed on data,', str(e)
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
    hyderabad_geo_box = [78.2176,17.18278,78.693248,17.624824] # for every location we need to update this
    # will make it config driven
    stream.filter(locations=hyderabad_geo_box, languages=["en"])

    # This line filter Twitter Streams to capture data by the keywords: 'keyword'
    # stream.filter(track=['keyword'])
