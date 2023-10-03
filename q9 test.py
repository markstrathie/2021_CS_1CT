f = open( "words.txt" )
dictionary = []
newSen = []
wrong = 0


nextLine = f.readline()
while nextLine != "" :
    dictionary.append( nextLine[ 0 : -1 ] )
    nextLine = f.readline()

sent = input( "Please enter a sentence to spell check: " )
wordList = sent.split()

for word in wordList:
    if word in dictionary:
        newSen.append( word )
    else:
        newSen.append( "**" + word + "**" )
        wrong = wrong + 1

for value in newSen:
    print( value + " ", end = "" )

print()
print( "Count of incorrectly spelled words: {0}".format( wrong ) )
