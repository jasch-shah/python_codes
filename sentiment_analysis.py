import csv
import tweepy


from textblob import TextBlob 


def Tweep():

	consumer_key = 'YOUR CONSUMER KEY'
	consumer_secret = 'YOUR SECRET KEY'

	access_token = 'YOUR ACCESS TOKEN'
	access_token_secret = 'ACCESS TOKEN SECRET'

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

	return tweepy.API(auth)


def labeling(text):
		
		blob = TextBlob(text).sentiment

		if blob.subjectivity == 0:
				return 0 # if no subjectivity we wont use tweet

		else:
				return 'Positive' if blob.polarity > 0 else 'Negative'




def give_me_csv(user, topic):
		
		list_of_tweets = user.search(topic, count = 100)
		filename = 'twitter_sentiment_%s.csv' % topic.replace(' ','')

		with open(filename, 'w') as file:
				fieldnames = ['tweet', 'sentiment_score']

				writer = csv.DictWriter(file, fieldnames = fieldnames)
				writer.writeheader()

				for tweet in list_of_tweets:
						tweet_text = tweet.text.encode('utf-8')
						score = labeling(tweet.text)

						if score != 0:
								writer.writerow({
										'tweet' : tweet_text,
										'sentiment_score' : score
										})

def main():
	#Login Twitter
	user = Tweep()

	#ask topic

	topic = raw_input('Enter topic to search:')

	#generate file

	give_me_csv(user, topic)



if __name__ == '__main__':
		main()	
