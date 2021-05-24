import datetime
import tweepy
import time
from PIL import Image, ImageDraw, ImageFont

auth = tweepy.OAuthHandler("olw6lknndaKvalPeQJnUVSkl0", "JSGhd15ngYz2tQPMhtJF3uRlpjizWoIkAEUOXSZzs7vqkgWRUF")
auth.set_access_token("1253657081552539648-C7L43ALfYhO0EffDdcvhqBnelKTHJs", "5io5HIKkTOlSAaTdNrQpkvxCL36aQBO1BixC58YX4CM4p") 
api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

now = datetime.datetime.now()

a = True
while True:
    a = str(now.day) + " " + str(now.month) + " " + str(now.hour) + " " + str(now.minute)
    ab = str(a) + " " + "@FaresBichard"
    if now.minute == 23 and a:
        img = Image.new('RGB', (1920, 1080), color = (73, 109, 137))
        fnt = ImageFont.truetype('C:/Users/juvic/OneDrive/Bureau/[Bureau]/Victor/programation/python/bot twitter/2 - date et heur/Font/Segoe_UI.ttf', 200)
        d = ImageDraw.Draw(img)
        d.text((550,450), str(a), font=fnt, fill=(255, 255, 0))
        img.save('t.png')
        api.update_with_media("C:/Users/juvic/OneDrive/Bureau/[Bureau]/Victor/programation/python/bot twitter/2 - date et heur/t.png")
        api.update_status("@FaresBichard", now)
        a = False
        print("c'est fait")
    elif now.minute == 1 and now.hour == 1:
        api.update_status(ab)
    elif now.minute == 2 and now.hour == 2:
        api.update_status(ab)
    elif now.minute == 3 and now.hour == 3:
        api.update_status(ab)
    elif now.minute == 4 and now.hour == 4:
        api.update_status(ab)
    elif now.minute == 5 and now.hour == 5:
        api.update_status(ab)
    elif now.minute == 6 and now.hour == 6:
        api.update_status(ab)
    elif now.minute == 7 and now.hour == 7:
        api.update_status(ab)
    elif now.minute == 8 and now.hour == 8:
        api.update_status(ab)
    elif now.minute == 9 and now.hour == 9:
        api.update_status(ab)
    elif now.minute == 10 and now.hour == 10:
        api.update_status(ab)
    elif now.minute == 11 and now.hour == 11:
        api.update_status(ab)
    elif now.minute == 12 and now.hour == 12:
        api.update_status(ab)
    elif now.minute == 13 and now.hour == 13:
        api.update_status(ab)
    elif now.minute == 14 and now.hour == 14:
        api.update_status(ab)
    elif now.minute == 15 and now.hour == 15:
        api.update_status(ab)
    elif now.minute == 16 and now.hour == 16:
        api.update_status(ab)
    elif now.minute == 17 and now.hour == 17:
        api.update_status(ab)
    elif now.minute == 18 and now.hour == 18:
        api.update_status(ab)
    elif now.minute == 19 and now.hour == 19:
        api.update_status(ab)
    elif now.minute == 20 and now.hour == 20:
        api.update_status(ab)
    elif now.minute == 21 and now.hour == 21:
        api.update_status(ab)
    elif now.minute == 22 and now.hour == 22:
        api.update_status(ab)
    elif now.minute == 23 and now.hour == 23:
        api.update_status(ab)
    elif now.minute == 0 and now.hour == 0:
        api.update_status(ab)
    else:
        a = True
