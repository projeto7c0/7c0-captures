import database_auth
import json


def insere_um(tweet, db):
    cursor = db.cursor()

    try:
        sql = """INSERT INTO `tweets` (`idTweets`, `plain_text`,
            `timestamp_tw`, `handle`, `retweets`, `favs`, `object`)
            VALUES (%s, %s, %s, %s, %s, %s, %s);"""
        try:
            cursor.execute(sql, (tweet.id_str, tweet.full_text, str(tweet.created_at), tweet.user.screen_name,
                           str(tweet.retweet_count), str(tweet.retweet_count), json.dumps(tweet._json)))
        except Exception as E:
            print(E)
    except Exception as E:
        print(E)


def insere_lista(tweets):
    db = database_auth.conecta_banco()
    for tweet in tweets:
        insere_um(tweet, db)
    db.commit()
    db.close()


def recupera_ids_total():
    db = database_auth.conecta_banco()
    sql = "select max(idTweets) from mimic_tweets;"
    cursor = db.cursor()
    value = ""
    try:
        cursor.execute(sql)
        value = cursor.fetchone()
    except Exception as E:
        print(E)
    db.close()
    return value[0]
