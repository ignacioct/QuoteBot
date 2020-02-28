#Version 1.0: funciona de forma local, evita duplicados usando aleatorio

import random, os

from tweepy.auth import OAuthHandler, API
import tweepy
from keys import * #there must be a keys.py with the keys



auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


api = API(auth)

#   Open Random Directory Function
#       @output: stream to the selected .txt file containing the lyrics 
def openRndDir():
    
    dir = os.getcwd()
    files = os.listdir(dir) 
    random_file = random.choice(files)
    return open(random_file, "r")

#   Get Random Quote Function
#       @input: stream to the selected .txt file containing the lyrics 
#       @output: string of the selected quote
def getRndQuote (file):
    quote = file.read()
    line = random.randrange(1, quote.count('$'), 1)
    quote = quote.split('$')[line][:-2]
    file.close()
    return quote

#   Get Quote Function
#       @input: string with the name of the folder in the current directory
#       @output: string of the selected quote
def getQuote(folder):
    return getRndQuote(openRndDir())


def main():
    os.chdir("bot")
    os.chdir("lyrics")
    while True:
        quote = getQuote("lyrics")
        print (quote)
        try:
            api.update_status(quote) #tweet to your TL
            break
        except tweepy.TweepError:
            print ("Error: Tweet duplicated\nChoosing another quote")

if __name__== "__main__":
    main()




