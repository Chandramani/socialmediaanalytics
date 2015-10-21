

for dir in `ls -d user*`;
do
cd $dir
python retweet_tweets_for_handles.py &
cd ..
done
