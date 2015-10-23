
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from keys import keys
import time

#Variables that contains the user credentials to access Twitter API
consumer_key = keys['consumer_key']
consumer_secret = keys['consumer_secret']
access_token = keys['access_token']
access_token_secret = keys['access_token_secret']


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
                        try:

                                saveFile = open('raw_tweets1.json', 'a')
                                print data
                                saveFile.write(data)
                                saveFile.close()

                                return True


                        except BaseException, e:
                                print 'failed ondata,', str(e)
                                time.sleep(5)
                                pass


    def on_error(self, status):
        print status


if __name__ == '__main__':

    # This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    hyderabad_geo_box = [78.2176,17.18278,78.693248,17.624824]
    # This line filter Twitter Streams to capture data by the keywords: 'keyword'
    # stream.filter(track=['keyword'])
    stream.filter(locations=hyderabad_geo_box,languages=["en"])
