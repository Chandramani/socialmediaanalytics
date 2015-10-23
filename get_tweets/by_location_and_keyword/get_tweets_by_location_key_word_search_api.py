__author__ = 'ctiwary'

import tweepy
import sys
from time import sleep
# from tweepy.auth import AppAuthHandler,OAuthHandler

from keys import keys

access_token = keys['access_token']
access_token_secret = keys['access_token_secret']
consumer_key = keys['consumer_key']
consumer_secret = keys['consumer_secret']
# Replace the API_KEY and API_SECRET with your application's key and secret.
# auth = tweepy.AppAuthHandler(access_token, access_token_secret)
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# api = tweepy.API(auth, wait_on_rate_limit=True,
# wait_on_rate_limit_notify=True)
#
# if (not api):
#     print ("Can't Authenticate")
#     sys.exit(-1)
# else:
#     print "authenticated"


api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, retry_count=3, retry_delay=5,
                 retry_errors=set([401, 402, 500, 503]))

hyderabad_geo_box = [78.2176, 17.18278, 78.693248, 17.624824]
hyderabad_geo_code = "17.4239299,78.4738385,705mi"
#
# #tweets = tweepy.Cursor(q="#SingleBecause",geocode=hyderabad_geo_box)
# # tweets = api.search(q="#SingleBecause",geocode=hyderabad_geo_code)
# # print tweets
#
while True:

    # count = 0
    # print "running for active words"
    # list_id = list()
    # user_set = set(line.strip() for line in open('file_active_user.txt'))
    # print user_set
    # with open('max_id_val.txt','r') as f:
    #     since_id_val = f.read()
    # print since_id_val
    # for tweets in tweepy.Cursor(api.search, q="JugaadNation", include_entities=True, result_type="mixed",
    #                             since_id=since_id_val).items():
    #     count += 1
    #     list_id.append(tweets.id)
    #     if ("hyderabad" in tweets.user.location.lower()) or ("andhra" in tweets.user.location.lower()) or \
    #             ("telangana" in tweets.user.location.lower()):
    #         print tweets.user.screen_name
    #         user_set.add(str(tweets.user.screen_name))
    #         # print tweets
    #         # try:
    #         #     saveFile.write("@"+tweets.user.screen_name+"\n")
    #         # except UnicodeEncodeError:
    #         #     print "could not write",tweets.user.screen_name, "|", tweets.user.location, "|", tweets.text
    # print count
    # if len(list_id) > 0:
    #     since_id_val = str(max(list_id))
    #
    # saveId = open('max_id_val.txt', 'w')
    # saveId.write(since_id_val)
    # saveId.close()
    # print user_set
    # saveFile = open('file_active_user.txt', 'w')
    # for user in user_set:
    #     saveFile.write(user+"\n")
    # saveFile.close()

    count = 0
    print "running reservation and relevant word"
    list_id = list()
    user_set = set(line.strip() for line in open('file_interested_user.txt'))
    # print user_set
    with open('max_id_val_reservation.txt','r') as f:
        since_id_val = f.read()
    # print since_id_val
    for tweets in tweepy.Cursor(api.search, q="reservation AND (caste OR sc OR st OR bc OR backward OR scheduled OR tribe OR private OR sector OR obc OR quota)",
                                include_entities=True, result_type="mixed", since_id=since_id_val).items():
        list_id.append(tweets.id)
        if ("hyderabad" in tweets.user.location.lower()) or ("andhra" in tweets.user.location.lower()) or \
                ("telangana" in tweets.user.location.lower()):
            count += 1
            print tweets.user.screen_name
            user_set.add(str(tweets.user.screen_name))
            # print tweets
            # try:
            #     saveFile.write("@"+tweets.user.screen_name+"\n")
            # except UnicodeEncodeError:
            #     print "could not write",tweets.user.screen_name, "|", tweets.user.location, "|", tweets.text
    # print count
    if len(list_id) > 0:
        since_id_val = str(max(list_id))

    saveId = open('max_id_val_reservation.txt', 'w')
    saveId.write(since_id_val)
    saveId.close()
    # print user_set
    saveFile = open('file_interested_user.txt', 'w')
    for user in user_set:
        saveFile.write(user+"\n")
    saveFile.close()

    count = 0
    print "running quota and relevant word"
    list_id = list()
    user_set = set(line.strip() for line in open('file_interested_user.txt'))
    # print user_set
    with open('max_id_val_quota.txt','r') as f:
        since_id_val = f.read()
    # print since_id_val
    for tweets in tweepy.Cursor(api.search, q="quota AND (caste OR sc OR st OR bc OR backward OR scheduled OR tribe OR private OR sector OR obc OR reservation)",
                                include_entities=True, result_type="mixed", since_id=since_id_val).items():
        list_id.append(tweets.id)
        if ("hyderabad" in tweets.user.location.lower()) or ("andhra" in tweets.user.location.lower()) or \
                ("telangana" in tweets.user.location.lower()):
            count += 1
            print tweets.user.screen_name
            user_set.add(str(tweets.user.screen_name))
            # print tweets
            # try:
            #     saveFile.write("@"+tweets.user.screen_name+"\n")
            # except UnicodeEncodeError:
            #     print "could not write",tweets.user.screen_name, "|", tweets.user.location, "|", tweets.text
    # print count
    if len(list_id) > 0:
        since_id_val = str(max(list_id))

    saveId = open('max_id_val_quota.txt', 'w')
    saveId.write(since_id_val)
    saveId.close()
    # print user_set
    saveFile = open('file_interested_user.txt', 'w')
    for user in user_set:
        saveFile.write(user+"\n")
    saveFile.close()
    print "sleeping for 5 minutes"
    sleep(300)

        # print tweets.user.screen_name,tweets.user.location
        # for tweet in tweets:
        #     print tweet
        #
        # for status in tweepy.Cursor(api.search, q="#SingleBecause", geocode=hyderabad_geo_code).items(10000):
        #     print status

        # api = tweepy.API(auth,
        #                  # support for multiple authentication handlers
        #                  # retry 3 times with 5 seconds delay when getting these error codes
        #                  # For more details see
        #                  # https://dev.twitter.com/docs/error-codes-responses
        #                  retry_count=3, retry_delay=5, retry_errors=set([401, 404, 500, 503]),
        #                  # monitor remaining calls and block until replenished
        #                  wait_on_rate_limit=True
        #                  )
        #
        # query = 'cupcake OR donut'
        # page_count = 0
        # for tweets in tweepy.Cursor(api.search, q=query, count=100, include_entities=True,geocode=hyderabad_geo_code).pages():
        #     page_count += 1
        # # print just the first tweet out of every page of 100 tweets
        #     print tweets[0].text.encode('utf-8')
        #     # stop after retrieving 200 pages
        #     if page_count >= 200:
        #         break