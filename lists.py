import twitter
import database

def get_new_tweets():
    topo = database.recupera_ids_total()
    tweets = twitter.list_tweets_list(topo)
    database.insere_lista(tweets)

def get_new_tweets_election():
    topo = 0
    tweets = twitter.list_tweets_election(topo)
    database.insere_lista(tweets)
