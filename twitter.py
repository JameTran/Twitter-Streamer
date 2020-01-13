import tweepy
from textblob import TextBlob
from tweepy.streaming import StreamListener
from tweepy import Stream

#  Twitter login info
consumer_key = 'SgGPLEywoVoJwJULMCoPof5vN'
consumer_secret = 'uVEWE7OJojnqSCqAMqVW4JTdS9eYjwrqJHOVaoCdkx0galxnE9'

access_token = '1041168468739932161-IHJP2EaK1NzW1fWdTbHZ2q3EDby7Od'
access_token_secret = 's4DeJvLdsZ5QdHpNGS1F9BYAtTRs4eALh5gxzyYNGHAnm'


class StdOutListener(StreamListener):  # Inherits from built in StreamListener
    def __init__(self, tweet_filename):
        self.tweet_filename = tweet_filename

    def on_data(self, data):  # writes to tweet_filename
        try:
            with open(self.tweet_filename, 'a') as fp:  
                fp.write(data)

        except BaseException as identifier:
            print("Error on data; %s" % identifier)

    def on_error(self, status):  # prints out the error message
        pass


# TWITTER STREAMER ##
# An object that processes live tweets
class TwitterStreamer():
    def __init__(self):
        pass

    def stream_tweets(self, tweet_filename, hash_tag_list):
        listener = StdOutListener(tweet_filename)  # creates a listener object
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)  # login
        auth.set_access_token(access_token, access_token_secret)
        # api = tweepy.API(auth)
        stream = Stream(auth, listener)
        stream.filter(track=hash_tag_list)


if __name__ == "__main__":
    hash_tag_list = ["Donald Trump", "Bernie Sanders"]
    tweet_filename = "tweets.json"
    
    streamer = TwitterStreamer()
    streamer.stream_tweets(tweet_filename, hash_tag_list)


# public_tweets = api.search('WW3')

# for tweet in public_tweets:
    # print(tweet.text)
    # analysis = TextBlob(tweet.text)
    # print(analysis.sentiment)
