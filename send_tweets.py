#!/usr/bin/env python
import tweepy, sys, time
from random import randint
from keys import keys

CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth,wait_on_rate_limit=True, wait_on_rate_limit_notify=True, retry_count=3, retry_delay=5,
                 retry_errors=set([401, 402, 500, 503]))

handles = "handles.txt"
f = open(handles, "r")
h = f.readlines()
f.close()

tweets_file = open("active_users.txt", "r")
tweets_to_be_sent = tweets_file.readlines()
tweets_file.close()

number_of_users = len(h)
if number_of_users > 2400:
    number_of_users = 2400

for i in h[0:number_of_users]:
    i = "@" + i.rstrip()
    print i
    m = i + " " + tweets_to_be_sent[0]
    s = api.update_status(status=m)
