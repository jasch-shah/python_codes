import tweepy
from textblob import TextBlob

consumer_key = '7hYpJLu2mDoUZmZpt8vfI989y'
consumer_secret = 'uzHxOIId6H2k6R14qg7t5D8XvLhjpj8fj6jhWBK1CmrEAEKsPZ'

access_token = '3253529420-XREr7zGSLED4qiXD9dyfTZxFAKnxtKRIloX6omY'
access_token_secret = 'zfBVOsg4lllJ7gMu9pcmfyiLJnWMQiGsPb9mmbb3y3ePZ'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Avengers Infinity War')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)