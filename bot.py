import tweepy
import random
import time
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import threading
import json

with open("config.json") as cf_file:
    config = json.load(cf_file)

pallates = config["COLORS"]

font = ImageFont.truetype("JetBrainsMono-Bold.ttf", 512)
font_small = ImageFont.truetype("JetBrainsMono-Bold.ttf", 64)

consumer_key = config["CONSUMER_KEY"]
consumer_secret = config["CONSUMER_SECRET"]

bearer_token = config["BEARER"]

access_token = config["ACCESS"]
access_secret = config["ACCESS_SECRET"]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(
    access_token,
    access_secret,
)

newapi = tweepy.Client(
    bearer_token=bearer_token,
    access_token=access_token,
    access_token_secret=access_secret,
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
)

api = tweepy.API(auth)

def make_tweet():
    tweet = ""

    pal = random.choice(pallates)

    length = random.randint(config["MIN_LENGTH"], config["MAX_LENGTH"])

    width = config["PADDING"] + (length * (config["FONT_SIZE"] + config["PADDING"]))
    
    image = Image.new("RGBA", (width, config["HEIGHT"]), color=pal[0])

    chars = config["CHAR_POOL"]

    for i in range(length):
        tweet += random.choice(chars)

    print(tweet)
    canvas = ImageDraw.Draw(image)
    canvas.text((width / 2, config["HEIGHT"] / 2), tweet, font=font, fill=pal[1], anchor="mm")

    canvas.text((config["PADDING"], config["HEIGHT"] - config["PADDING"] - config["SMALL_FONT_SIZE"]), "actually random letters every 10 minutes", font=font_small, fill=pal[1])

    image.save("tweet.png")

    image_to_upload = api.media_upload("tweet.png")
    image_id = image_to_upload.media_id
    print(newapi.create_tweet(text=tweet, media_ids=[image_id]))

def run():
    while True:
        make_tweet()
        time.sleep(config["TIME_BETWEEN_TWEETS"])

make_tweet()

thread = threading.Thread(target=run)
#thread.start()
