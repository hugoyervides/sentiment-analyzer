from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sentiment_engine as s

#consumer key, consumer secret, access token, access secret.
ckey="6FYXexXbYU13x4mN4THTVz9E0"
csecret="MTwJV66fiKzToRqlW7EsTIBoGIa1OEwrbo2CLALAVgKUJaAeaI"
atoken="3004163805-lDfo3HgTxU8yU3YxRq7goRw4tFl3WFvlLeMvsUS"
asecret="CPWDspxEa61MMZxxQtFCJZ09v1hd1vBYGjOIASIjNlQbJ"

class listener(StreamListener):
    def on_data(self, data):
        all_data = json.loads(data)
        tweet = all_data["text"]
        sentiment_value, confidence = s.sentiment(tweet)
        print(tweet, sentiment_value, confidence)
        
        if confidence*100 >= 80:
            output = open("data/twitter-central-america.txt","a")
            output.write(sentiment_value)
            output.write('\n')
            output.close()

        return True

    def on_error(self, status):
        print (status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(locations=[-92.7369202437,6.6431421332,-76.5650452437,18.4591111738])