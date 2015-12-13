# TweetCollector
A tweet collection program in Python

This program collects fifteern tweets for every fifteen minutes and writes those tweets to a file with the tweet id of the latest tweet as the file name.

The program then reads tweets from the text file, concatenates five tweet texts and sends an SMS.

The program then sleeps for five minutes and then repeats the same.

This program is run every fifteen minutes (using a scheduled job like cron) and when it is run, it reads the name of the only txt file in the same directory (which has the latest tweet id as the file name). And this id will be used as one of the parameters for searching tweets (since_id).

Python modules required - Tweepy and Plivo
