import math

# finds total number of tweets needed
def totaltweets(tweetlen):
    tweetlen = float(tweetlen)
    if (tweetlen <= 1):
        numtweets = 1
    elif (tweetlen <= 1206): # from 1 - 9 individual tweets
        div = float(tweetlen)/134
        numtweets = math.ceil(div)
        print("numtweets "+str(numtweets))
    elif (tweetlen <= 13077): # from 10 - 99 individual tweets
        div = (float(tweetlen)-9*(140-7))/(140-8)
        numtweets = math.ceil(div)+9
    elif (tweetlen <= 129978): # from 100 - 999 individual tweets
        div = (float(tweetlen)-9*(140-8)-90(140-9))/(140-10)
        numtweets = math.ceil(div)+99
    else:
        print('stfu you don\'t have that much to say')
    numtweets = int(numtweets)
    return numtweets

# puts the tweets into blocks and outputs them
def tweetblock(numtweets, tweet, tweetlen):
    index = 1
    start = 0
    end = 135
    for i in range(0, numtweets):
        print(tweet[start:end]+" ("+str(index)+"/"+str(numtweets)+ ")")
        start+=135
        end+=135
        index+=1
        #print ("start" + str(start)+" end "+str(end)+ " index " + str(index))
    return 0

# main I guess lol
def main():
    # gets some character thing
    tweet = raw_input('Please enter a tweet ')
    tweetlen = len(tweet)
    print("total characters: "+str(tweetlen))
    numtweets = totaltweets(tweetlen)
    print(numtweets)
    tweetblock(numtweets, tweet, tweetlen)

if __name__ == "__main__":
    main()
