import tweepy
import sys

config = {
    'consumer_key': 'tEUKumPKEMfrELskEjXdeUaCi',
    'consumer_secret': 'lVlh4Cqx7O2eMUw8Uqcx7CK40B2kIOXbdiZbnzi9xbtnjq2zZU',
    'access_token': '262123703-T6Dx9kaNijYq4rhpt7LgTu6fgMVcf77gNrBHimQq',
    'access_secret': 'aWCHwvDERGyl8KHkDu09FHXiWfszCj84deBEnTmXblN93'
}

auth = tweepy.OAuthHandler(config['consumer_key'], config['consumer_secret'])
auth.set_access_token(config['access_token'], config['access_secret'])

api = tweepy.API(auth)

api.update_status(status=' '.join(sys.argv[1:]))
