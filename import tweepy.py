import tweepy
import pandas as pd
import numpy as np
import time

bearer_token = 'ur token here'

client = tweepy.Client(bearer_token=bearer_token)

twitter_account = 'elonmusk'

user = client.get_user(username=twitter_account)
user_id = user.data.id

try:
    tweets = client.get_users_tweets(id=user_id, max_results=100, tweet_fields=['text'])
except tweepy.errors.TooManyRequests:
    print("Rate limit exceeded. Waiting for 15 minutes.")
    time.sleep(15 * 60) 
    tweets = client.get_users_tweets(id=user_id, max_results=100, tweet_fields=['text'])

tweets_data = pd.DataFrame(data=[tweet.text for tweet in tweets.data], columns=['Tweet'])

tweets_data.to_excel('elonmusk_tweets.xlsx', index=False)

print(tweets_data)
