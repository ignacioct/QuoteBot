import random, os


def main():
    os.chdir("bot")
    os.chdir("lyrics")

    dir = os.getcwd()
    
    file= open("que_mas_da.txt", "r")

    quote = file.read()
    for i in range (1, quote.count('$')+1, 1):
        print(quote.split('$')[i][:-2])
    file.close()
    return quote

if __name__== "__main__":
    main()
