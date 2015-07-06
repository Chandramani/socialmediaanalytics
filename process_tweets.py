__author__ = 'ctiwary'

import json

# with open("data/raw_tweets1.json", 'r') as json_file:
#     for json_string in json_file:
#         json_obj = json.loads(json_string)
#         user_file = open("processed_author_tweets/"+str(json_obj["user"]["id"]), "a")
#         user_file.write(str(json_obj["text"].encode("utf-8"))+"\n")
#         # user_filwrite("text"+"\n")
#         user_file.close()

user_set = set(line.strip() for line in open('data/active_users.txt'))
with open("data/raw_tweets1.json", 'r') as json_file:
    for json_string in json_file:
        json_obj = json.loads(json_string)
        user_set.add(json_obj["user"]["screen_name"])

user_file = open("data/active_users.txt", "w")
for user in user_set:
    user_file.write(str(user)+"\n")
# user_filwrite("text"+"\n")
user_file.close()

