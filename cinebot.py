import tweepy
import schedule
import time
import imdb
from dotenv import load_dotenv
import os

<<<<<<< HEAD
consumer_key = os.getenv('consumer_key')
consumer_secret = os.getenv('consumer_secret')

key = os.getenv('key')
secret = os.getenv('secret')
=======
>>>>>>> a691813e790b36b14931743bb4cf6afd649107aa

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api= tweepy.API(auth, wait_on_rate_limit=True)


def run():

    moviesDB = imdb.IMDb()

    #get list of the best movies
    top = moviesDB.get_top250_movies()

    print('Top 100 movies: ')
    for movie in top[0:101]:
        title = movie["title"]
        year = movie["year"]
        rating = movie["rating"]
        #directors = movie["directors"]
        print(f"🎥{title} - {year}")
        print(f"🌟Rating: {rating}")
        # direcStr = " ".join(map(str,directors))
        # print(f"directors: {direcStr}") 


if __name__ == "__main__":
    run()
