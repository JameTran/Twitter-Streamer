import tweepy
from textblob import TextBlob
from tweepy.streaming import StreamListener


consumer_key = 'SgGPLEywoVoJwJULMCoPof5vN'
consumer_secret = 'uVEWE7OJojnqSCqAMqVW4JTdS9eYjwrqJHOVaoCdkx0galxnE9'

access_token = '1041168468739932161-IHJP2EaK1NzW1fWdTbHZ2q3EDby7Od'
access_token_secret = 's4DeJvLdsZ5QdHpNGS1F9BYAtTRs4eALh5gxzyYNGHAnm'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)  # login
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


class StdOutListener(StreamListener):
    def on_data(self, data):  # takes in info from streamlistener
        print(data)

    def on_error(self, status):
        pass


# TWITTER STREAMER ##
class TwitterStreamer():
    def __init__(self):
        pass

    def stream_tweets(self, a, b):
        

# asdasd ## asdasd





# public_tweets = api.search('WW3')

# for tweet in public_tweets:
    # print(tweet.text)
    # analysis = TextBlob(tweet.text)
    # print(analysis.sentiment)
