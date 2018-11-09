from textblob import TextBlob

def get_tweet_sentiment(tweet): analysis = TextBlob(tweet)
if analysis.sentiment.polarity > 0: print('positive')
elif analysis.sentiment.polarity == 0: print('neutral')
else:
print('negative') get_tweet_sentiment("He wasn't a bad boy")
