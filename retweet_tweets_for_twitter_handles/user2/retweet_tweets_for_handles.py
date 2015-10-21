__author__ = 'ctiwary'

#!/usr/bin/env python
import tweepy,sys, time
from random import randint
from keys import keys
import getopt, sys

def return_cred():
    CONSUMER_KEY = keys['consumer_key']
    CONSUMER_SECRET = keys['consumer_secret']
    ACCESS_TOKEN = keys['access_token']
    ACCESS_TOKEN_SECRET = keys['access_token_secret']
    return CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

def retweet():
        handles_file = open("handles.txt", "r")
        handles = handles_file.readlines()
        for handle in handles:
                print "re tweeting handle", handle
                for status in api.user_timeline(handle):
                    try:
                        api.retweet(status.id)
                    except Exception as e:
                        print e
                nap = randint(59, 160)
                print "sleeping for", nap,"seconds"
                time.sleep(nap)


retry = 0
sleep = 60
if __name__ == "__main__":
    try:
        CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET = return_cred()
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, retry_count=3, retry_delay=5,
                         retry_errors=set([401, 402, 500, 503, 226]))
    except Exception as e:
        print "connection error quitting"
    try:
        retweet()
    except Exception as e:
        print e