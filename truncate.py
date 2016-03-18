import math

# important variables

# character length per tweet
oneOnes = 140-6
tenOnes = 140-7
tenTens = 140-8
hunOnes = 140-8
hunTens = 140-9
hunHuns = 140-10

# max length for each bracket
oneslen = 9*(oneOnes)
tenslen = 9*(tenOnes)+90*(tenTens)
hunslen = 9*(hunOnes)+90*(hunTens)+900*(hunHuns)

# finds total number of tweets needed
def totaltweets(tweetlen):
    tweetlen = float(tweetlen)
    if (tweetlen <= 1):
        numtweets = 1
    elif (tweetlen <= oneslen): # from 1 - 9 individual tweets
        div = float(tweetlen)/oneOnes
        numtweets = math.ceil(div)
        print("numtweets "+str(numtweets))
    elif (tweetlen <= tenslen): # from 10 - 99 individual tweets
        div = (float(tweetlen)-9*tenOnes)/tenTens
        numtweets = math.ceil(div)+9
    elif (tweetlen <= hunslen): # from 100 - 999 individual tweets
        div = (float(tweetlen)-9*hunOnes-90*hunTens)/hunHuns
        numtweets = math.ceil(div)+99
    else:
        print('stfu you don\'t have that much to say')
        numtweets = 0
    numtweets = int(numtweets)
    return numtweets

# puts the tweets into blocks and outputs them
def tweetblock(numtweets, tweet, tweetlen):
    # how much to skip per slice 
    if (tweetlen <= oneslen):
        jump = oneOnes  
    elif (tweetlen <= tenslen):
        jump = tenOnes  
    elif (tweetlen <= hunslen):
        jump = hunOnes  

    index = 1 # number of tweet
    start = 0 # start of slice
    end = jump # slice length
    for i in range(0, numtweets):
        print(tweet[start:end]+" ("+str(index)+"/"+str(numtweets)+ ")")
        index+=1
        if (index==10 or index==100): 
            start+=1 # takes into account that this would have been printed, in the change with jump
            jump-=1
        start+=jump
        end+=jump
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
