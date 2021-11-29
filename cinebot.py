from math import remainder
from typing import ByteString
import tweepy
import schedule
import time
import imdb
from dotenv import load_dotenv
import os
import random

inicio = time.time()

#Check keys
load_dotenv()
API_KEY = os.getenv('API_key')
API_SECRET = os.getenv('API_secret')
key = os.getenv('key')
secret = os.getenv('secret')
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(key, secret)
api= tweepy.API(auth, wait_on_rate_limit=True)

insultos = ["tonto", "subnormal", "mierda", "conchatumadre", "basura", "apesta"]

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

#Retweet topics
def retweet(hashtag,api):
    for tweet in tweepy.Cursor(api.search, q=(hashtag)).items(10):
        try:
            tweet.retweet()
            time.sleep(5)
        except:
            print("Can't retweet  "+str(tweet.id)+" by user"+tweet.user.screen_name)
#Read mentions
def read_last_id():
    file = open("last_id.txt", "r")
    id = int(file.read().strip())
    file.close()
    return id

#save last id
def store_last_id(id):
    file = open("last_id.txt", "w")
    file.write(str(id))
    file.close()
    

#reply mentions
moviesDB = imdb.IMDb()
# get list of the best movies
top = moviesDB.get_top250_movies()
# k = number of movies to select
top_1 = random.choices(top, k=1)
for movie in top_1:
    title = movie["title"]
    year = movie["year"]
    rating = movie["rating"]
best_movie = str(f"🎥 {title} - {year} ") + str(f" 🌟 IMDb rating: {rating}")

def reply_best_movies(tweet):
    api.update_status("@" + tweet.user.screen_name +  " Te recomiendo: " + best_movie, tweet.id)
    store_last_id(tweet.id) 

#reply and block trolls
def reply_and_block(tweet):
	api.update_status('@' + tweet.user.screen_name + ' ' + 'Hasta nunca, gil 😡', tweet.id)
	store_last_id(tweet.id)
	api.create_block(tweet.user.screen_name)
        

#Check mentions
def check_mentions():
    mentions = api.mentions_timeline(read_last_id(), tweet_mode = "extended")
    for tweet in reversed(mentions):
        print(tweet.full_text)
    if any(x in tweet.full_text for x in insultos):
        reply_and_block(tweet)
    else:
        reply_best_movies(tweet)

def run():
    
    schedule.every(7).seconds.do(check_mentions)
    schedule.every().day.at("06:02").do(tuitear)
    schedule.every().day.at("14:02").do(tuitear)
    schedule.every().day.at("22:02").do(tuitear)
    
    while True:
        try:
            schedule.run_pending()
            time.sleep(2)
        except tweepy.TweepyError as e:
            raise e

subjects = ["Cineperuano", "Oscars2022", "CineLatinoamericano", "Sitges2021", "LeónDeOro", "Cannes2021"]
for subject in subjects:
    retweet("#"+subject,api)


if __name__ == '__main__':
    run()

fin = time.time()
print(fin - inicio)