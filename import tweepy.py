import tweepy
import pandas as pd
import numpy as np
import time

# Replace these with your own Twitter API credentials
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAIAgzgEAAAAAfh81nH2cs6MQMTmYxaBzgcQqsO8%3DjuYg5FlOzAL7TbjVAU7k2AGAZVC4Rtt44D34n5hGV11DQQBk5d'

# Authenticate to Twitter
client = tweepy.Client(bearer_token=bearer_token)

# Define the Twitter account you want to fetch tweets from
twitter_account = 'elonmusk'

# Get the user ID for the Twitter account
user = client.get_user(username=twitter_account)
user_id = user.data.id

# Fetch the latest tweets from the account with a delay to avoid rate limits
try:
    tweets = client.get_users_tweets(id=user_id, max_results=100, tweet_fields=['text'])
except tweepy.errors.TooManyRequests:
    print("Rate limit exceeded. Waiting for 15 minutes.")
    time.sleep(15 * 60)  # Wait for 15 minutes
    tweets = client.get_users_tweets(id=user_id, max_results=100, tweet_fields=['text'])

# Create a DataFrame to store the tweets
tweets_data = pd.DataFrame(data=[tweet.text for tweet in tweets.data], columns=['Tweet'])

# Save the DataFrame to an Excel file
tweets_data.to_excel('elonmusk_tweets.xlsx', index=False)

# Print the DataFrame
print(tweets_data)