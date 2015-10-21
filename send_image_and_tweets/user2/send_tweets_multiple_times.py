#!/usr/bin/env python
import time
from random import randint
import getopt
import sys
import os
import glob
import re

import tweepy

from keys import keys


def return_cred():
    CONSUMER_KEY = keys['consumer_key']
    CONSUMER_SECRET = keys['consumer_secret']
    ACCESS_TOKEN = keys['access_token']
    ACCESS_TOKEN_SECRET = keys['access_token_secret']
    return CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

# handles = "active_users.txt"
# f = open(handles, "r")
# h = f.readlines()
# f.close()

# tweets_file = open("tweets_to_be_sent.txt", "r")
# tweets_to_be_sent = tweets_file.readlines()
# tweets_file.close()

# number_of_users = len(h)
# if number_of_users > 2000:
# number_of_users = 2000

# log_file = open("send_tweets_logs.txt","a")
# for i in range(5,2000):
#     print i
#     m = str(i) + "  " + tweets_to_be_sent[0]
#     s = api.update_status(status=m)
#     log_file.write(str(i)+"\n")
#     nap = randint(59, 160)
#     time.sleep(nap)
# log_file.close()

if __name__ == "__main__":
    global tweets_to_be_sent, image_file, type_of_tweet
    try:
        opts, remainder = getopt.getopt(sys.argv[1:], "", ["type="])
        for opt, arg in opts:
            if opt in '--type':
                type_of_tweet = arg

        CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET = return_cred()
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, retry_count=3, retry_delay=5,
                         retry_errors=set([401, 402, 500, 503, 226]))

        if type_of_tweet == "image":
            for i in range(1, 11):
                listing = glob.glob("../tweet*")
                for path in listing:
                    for filename in os.listdir(path):
                        print filename
                        if re.findall('([-\w]+\.(?:jpg|gif|png))', filename):
                            image_file = path+"/"+filename
                            print image_file
                        elif re.findall('([-\w]+\.(?:txt))', filename):
                            text_file = filename
                            tweets_file = open(path+"/"+text_file, "r")
                            tweets_to_be_sent = tweets_file.readlines()
                            print tweets_to_be_sent
                            tweets_file.close()
                    s = api.update_with_media(image_file, tweets_to_be_sent[0] + " "+ str(i))
                    # log_file.write(str(i)+"\n")
                    nap = randint(0, 59)
                    print "sleeping for", nap, "seconds"
                    time.sleep(nap)
                    # log_file.close()
        else:
            for i in range(1, 11):
                listing = glob.glob("../tweet*/*")
                for path in listing:
                    if re.findall('([-\w]+\.(?:txt))', path):
                        text_file = path
                        tweets_file = open("tweets_to_be_sent.txt", "r")
                        tweets_to_be_sent = tweets_file.readlines()
                        tweets_file.close()
                    m = str(i) + "  " + tweets_to_be_sent[0]#tweets_to_be_sent[0]
                    s = api.update_status(status=m)
                    # log_file.write(str(i)+"\n")
                    nap = randint(0, 59)
                    time.sleep(nap)

    except getopt.GetoptError as err:
        # print help information and exit:
        print str(err) # will print something like "option -a not recognized"
        # usage() write a function describing code usage
        sys.exit(2)


    # CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET = return_cred()
    # auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    # auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    # api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, retry_count=3, retry_delay=5,
    #                  retry_errors=set([401, 402, 500, 503, 226]))
    # image_file = 'narendra-modi-feku.jpg'
    #
    # for i in range(5, 2000):
    #     print i
    #     s = api.update_with_media(image_file, str(i))
    #     # log_file.write(str(i)+"\n")
    #     nap = randint(59, 160)
    #     time.sleep(nap)
    #     # log_file.close()
