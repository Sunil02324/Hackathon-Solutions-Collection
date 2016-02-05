from twython import Twython

TWITTER_APP_KEY = ''
TWITTER_APP_KEY_SECRET = ''
TWITTER_ACCESS_TOKEN = ''
TWITTER_ACCESS_TOKEN_SECRET = ''

t = Twython(TWITTER_APP_KEY, TWITTER_APP_KEY_SECRET, TWITTER_ACCESS_TOKEN,       TWITTER_ACCESS_TOKEN_SECRET)

search = t.search(q='hello', count=100)

tweets = search['statuses']

for tweet in tweets:
    print (tweet['text'], '\n')