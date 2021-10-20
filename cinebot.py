import tweepy
import schedule
import time
import imdb

consumer_key = "taPM56wXc4ZHeSXu5pBniXYCb"
consumer_secret = "lw7pKTTKQsGZLC8W5xDp02DufpMwun2RHW2a3M0hQ3mdIZpiaY"

key = "1447766124314169355-AKyBVNfAL8eM40GFOOERVCDdzEYS9Y"
secret = "xoUhCOid3nkZhvN10IK7KneRKqzG48kfESwSPfCavsCjD"

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
        # print(f"directors: {direcStr}")comprobar


if __name__ == "__main__":
    run()