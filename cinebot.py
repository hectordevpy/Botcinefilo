import tweepy
import schedule
import time
import imdb
from dotenv import load_dotenv
import os
import random
import pandas as pd
import requests
import lxml.html as html

#enviroment variables
load_dotenv()
API_KEY = os.getenv('API_key')
API_SECRET = os.getenv('API_secret')
key = os.getenv('key')
secret = os.getenv('secret')
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(key, secret)
api= tweepy.API(auth, wait_on_rate_limit=True)

#Extract iconic phrases from .txt
text_database = './phrases.txt'
lines_list = []
with open (text_database) as f:
    lines = f.readlines()
    lines_list.append(lines)
for item in lines_list:
    movie_quotes = item[random.randrange(len(item))]
    
# Tweet iconic phrases of movies 
def tuitear():
    api.update_status(movie_quotes)

def run():
    schedule.every().day.at("06:02").do(tuitear)
    schedule.every().day.at("14:02").do(tuitear)
    schedule.every().day.at("22:02").do(tuitear)

    while True:
        try:
            schedule.run_pending()
        except tweepy.TweepyError as e:
            raise e
if __name__ == '__main__':
    run()

#Retweet topics
def retweet(hashtag,api):
    for twit in tweepy.Cursor(api.search, q=(hashtag)).items(10):
        try:
            twit.retweet()
            time.sleep(10)
        except:
            print("Can't retweet  "+str(twit.id)+" by user"+twit.user.screen_name)

subjects = ["Cineperuano", "Oscars2022", "CineLatinoamericano", "Sitges2021", "LeónDeOro", "Cannes2021"]
for subject in subjects:
    retweet("#"+subject,api)

#     moviesDB = imdb.IMDb()

#     # get list of the best movies
#     top = moviesDB.get_top250_movies()
#     # k = number of movies to select
#     top_3 = random.choices(top, k=3)
#     print('Mis recomendaciones 🤓: ')
#     for movie in top_3:
#         title = movie["title"]
#         year = movie["year"]
#         rating = movie["rating"]
    
#         print(f"🎥{title} - {year}")
#         print(f"🌟Rating: {rating}")


