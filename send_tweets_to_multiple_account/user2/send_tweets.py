#!/usr/bin/env python
import time
from random import randint

import tweepy

from send_tweets_to_multiple_account.copy_to_folder import keys


CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth,wait_on_rate_limit=True, wait_on_rate_limit_notify=True, retry_count=3, retry_delay=5,
                 retry_errors=set([401, 402, 500, 503,226]))

handles = "active_users.txt"
f = open(handles, "r")
h = f.readlines()
f.close()

tweets_file = open("tweets_to_be_sent.txt", "r")
tweets_to_be_sent = tweets_file.readlines()
tweets_file.close()

number_of_users = len(h)
if number_of_users > 2000:
    number_of_users = 2000

log_file = open("send_tweets_logs.txt","a")
for i in h[55:number_of_users]:
    i = "@" + i.rstrip()
    print i
    m = i + " " + tweets_to_be_sent[0]
    s = api.update_status(status=m)
    log_file.write(str(i)+"\n")
    nap = randint(59, 160)
    time.sleep(nap) 
log_file.close()
