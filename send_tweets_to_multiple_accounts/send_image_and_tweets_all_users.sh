#!/usr/bin/env bash

len_of_handles=`wc -l < active_users.txt`
echo $len_of_handles
len_of_users=`find . -maxdepth 1 -name "user*" | wc -l`
echo $len_of_users

range=$(($len_of_handles/$len_of_users))
echo "range is $range"
start_index=0
end_index=$range


for dir in `ls -d user*`;
do
cd $dir
python send_tweets.py --type="image" --start=$start_index --end=$end_index &
cd ..
start_index=$(($start_index + $range))
end_index=$(($end_index + $range))
done
