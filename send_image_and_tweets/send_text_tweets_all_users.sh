

for dir in `ls -d user*`;
do
cd $dir
python send_tweets_multiple_times.py --type="text" &
cd ..
done
