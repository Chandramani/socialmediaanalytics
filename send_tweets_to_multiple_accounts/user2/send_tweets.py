#!/usr/bin/env python
import time
import tweepy
import glob
import os
import re
import getopt
import sys

from random import randint
from keys import keys

global tweets_to_be_sent, image_file, type_of_tweet, start_user, end_user


def send_image_and_text_tweets(user_name):
    listing = glob.glob("../tweet*")
    for path in listing:
        for filename in os.listdir(path):
            if re.findall('([-\w]+\.(?:jpg|gif|png))', filename):
                image_file = path+"/"+filename
            elif re.findall('([-\w]+\.(?:txt))', filename):
                text_file = filename
                tweets_file = open(path+"/"+text_file, "r")
                tweets_to_be_sent = tweets_file.readlines()
                tweets_file.close()
        s = api.update_with_media(image_file, user_name + " " + tweets_to_be_sent[0] + " "+ str(i))


def send_text_tweet(user_name):
    listing = glob.glob("../tweet*")
    for path in listing:
        for filename in os.listdir(path):
            if re.findall('([-\w]+\.(?:txt))', filename):
                text_file = filename
                tweets_file = open(path+"/"+text_file, "r")
                tweets_to_be_sent = tweets_file.readlines()
                tweets_file.close()
        m = user_name + "  " + tweets_to_be_sent[0]
        s = api.update_status(status=m)

CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

if __name__ == "__main__":

    try:
        opts, remainder = getopt.getopt(sys.argv[1:], "", ["type=", "start=", "end="])
        for opt, arg in opts:
            if opt == '--type':
                type_of_tweet = arg
            if opt == '--start':
                start_user = arg
            if opt == '--end':
                end_user = arg

        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        api = tweepy.API(auth,wait_on_rate_limit=True, wait_on_rate_limit_notify=True, retry_count=3, retry_delay=5,
                         retry_errors=set([401, 402, 500, 503,226]))

        handles = "../active_users.txt"
        f = open(handles, "r")
        h = f.readlines()
        f.close()

        for i in h[int(start_user):int(end_user)]:
            i = "@" + i.rstrip()
            if type_of_tweet == "image":
                send_image_and_text_tweets(user_name=i)
            else:
                send_text_tweet(user_name=i)
            nap = randint(59, 179)
            print "sleeping for", nap, "seconds"
            time.sleep(nap)

    except Exception as e:
        print e
