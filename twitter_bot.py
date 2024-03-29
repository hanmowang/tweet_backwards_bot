import io
import os
import tempfile
from unicodedata import name
import tweepy
from time import sleep
from credentials import *
from config import QUERY, FOLLOW, LIKE, SLEEP_TIME
from PIL import Image
import requests
from io import BytesIO
#mirror text
def mirror_text(text):
    str1 = ''
    str2 = ''
    for x in text:
        if x == '\n':
            str2 = str2 + str1[::-1]
            str2 = str2 + '\n'
            str1 = ''
        else:
            str1 = str1 + x
    str2 = str2 + str1[::-1]
    return str2

#set up api
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#changing the user's profile picture
tweets = api.user_timeline(screen_name = QUERY, count = 1, include_rts = False, 
                            tweet_mode = 'extended')
profile_pic = str.replace(tweets[0].user.profile_image_url,"_normal", "")
response = requests.get(profile_pic)
img = Image.open(BytesIO(response.content))
flipped_img = img.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
tf = tempfile.NamedTemporaryFile(suffix=".png", delete=False)
flipped_img.save(tf, format="png")
api.update_profile_image(tf.name)
tf.close()
os.unlink(tf.name)
#changing the user's name and description
name = tweets[0].user.name
desc = tweets[0].user.description
api.update_profile(name = mirror_text(name), description = mirror_text(desc))
#changing the user's profile banner
response = requests.get(tweets[0].user.profile_banner_url)
img = Image.open(BytesIO(response.content))
flipped_img = img.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
tf = tempfile.NamedTemporaryFile(suffix=".png", delete=False)
flipped_img.save(tf, format="png")
api.update_profile_banner(tf.name)
tf.close()
os.unlink(tf.name)

#infinite loop to detect new tweets
while True:
    #getting the 20 most recent tweets and replies
    tweets = api.user_timeline(screen_name = QUERY, count = 20, include_rts = False, 
                            tweet_mode = 'extended')
    for tweet in tweets:
        #only reply under the tweet we have not liked before
        #the tweet must also be an original tweet, not a reply under someone else's tweet.
        if tweet.in_reply_to_status_id is None and not tweet.favorited:
            tweet.favorite()
            #when there are photos in the tweet, we also make the photo backwards
            if 'media' in tweet.entities:
                media_ids = []
                media_details = tweet.extended_entities['media']
                for photo in media_details:
                    if photo['type'] != 'photo':
                        break
                    else:
                        response = requests.get(photo['media_url'])
                        img = Image.open(BytesIO(response.content))
                        flipped_img = img.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
                        b = BytesIO()
                        flipped_img.save(b, "jpeg")
                        b.seek(0)
                        fp = io.BufferedReader(b)
                        media = api.media_upload('test.png', file=fp)
                        media_ids.append(media.media_id_string)          
                print(tweet.full_text)
                print('\n')
                str = mirror_text(tweet.full_text)
                print(str)
                api.update_status(status=str, in_reply_to_status_id=tweet.id, 
                                   auto_populate_reply_metadata=True, media_ids=media_ids)
            #if there are no picture, simply mirror the text and we are done!
            else:
                print(tweet.full_text)
                print('\n')
                str = mirror_text(tweet.full_text)
                str = str + '\n--This is a bot'
                print(str)
                api.update_status(status=str, in_reply_to_status_id=tweet.id, 
                                   auto_populate_reply_metadata=True,)
    #10 minutes sleep time
    print("sleep")
    sleep(SLEEP_TIME)
    
