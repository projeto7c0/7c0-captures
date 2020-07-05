import tweepy
import twitter_auth

def list_tweets_list(topo):
    api = twitter_auth.autentica_list()

    tweets = []

    for status in tweepy.Cursor(api.list_timeline, tweet_mode='extended', owner_screen_name="projeto7c0", slug="politicos-br", since_id=topo, count=200).items():
        tweets.append(status)

    return tweets
