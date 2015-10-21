__author__ = 'ctiwary'

import tweepy
import json
import sys

oauth_keys = []
keys = json.load(open("../all_tokens/keys.json"))
for key in keys:
    oauth_key = []
    oauth_key.append(key.get("consumer_key"))
    oauth_key.append(key.get("consumer_secret"))
    oauth_key.append(key.get("access_token"))
    oauth_key.append(key.get("access_token_secret"))
    oauth_keys.append(oauth_key)

auths = []
for consumer_key, consumer_secret, access_key, access_secret in oauth_keys:
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    auths.append(auth)

api = tweepy.API(auths)

length = len(oauth_keys)

while length > 0:
    api.auth_idx = 2
    length -= 1



