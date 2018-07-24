#Program that searches for a tweet matching
#the term given and prints out the username and their tweet


from twython import TwythonStreamer
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret)
#on_success code runs when a matching tweet is found
class myStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            username = data['user']['screen_name']
            tweet = data['text']
            #prints out the username followed by the tweet text
            #print("@{}: {}".format(username, tweet))
            print(data['text']) #just gives the tweet text

#instance of myStreamer
stream = myStreamer(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret)
#status filter to track a particular term
stream.statuses.filter(track = 'Nairobi')
    
            
