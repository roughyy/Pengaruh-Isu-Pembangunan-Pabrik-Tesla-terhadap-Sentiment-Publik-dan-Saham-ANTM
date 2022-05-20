import snscrape.modules.twitter as sntwitter
import pandas as pd
import csv

# Creating list to append tweet data to
tweets_list2 = []

# Using TwitterSearchScraper to scrape data and append tweets to list
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('pabrik tesla since:2020-10-01 until:2021-01-01').get_items()):
    if i>1500:
        break
    tweets_list2.append([tweet.date,tweet.content, tweet.user.username])
    
# Creating a dataframe from the tweets list above
tweets_df2 = pd.DataFrame(tweets_list2, columns=['Datetime','Text','Username'])

tweets_df2.to_csv('hasil.csv')

