import tweepy
import sys

# Get config from https://apps.twitter.com/

config = {
    'consumer_key': 'XXX',
    'consumer_secret': 'XXX',
    'access_token': 'XXX',
    'access_secret': 'XXX'
}

auth = tweepy.OAuthHandler(config['consumer_key'], config['consumer_secret'])
auth.set_access_token(config['access_token'], config['access_secret'])

api = tweepy.API(auth)

api.update_status(status=' '.join(sys.argv[1:]))
