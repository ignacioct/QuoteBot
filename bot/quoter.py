import random, os

from tweepy.auth import OAuthHandler, API
from keys import * #there must be a keys.py with the keys



auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


api = API(auth)

#   Open Random Directory Function
#       @input: string with the name of the folder in the current directory
#       @output: stream to the selected .txt file containing the lyrics 
def openRndDir (folder):
    os.chdir(folder)
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
    return getRndQuote(openRndDir(folder))




def main():
    quote = getQuote("lyrics")

    print (quote)
    api.update_status(quote) #tweet to your TL

if __name__== "__main__":
    main()




