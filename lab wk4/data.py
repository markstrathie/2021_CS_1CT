oldFile = open( "data.txt" )
newFile = open( "dataWithAverages.txt", "w" )

line = oldFile.readline()
newFile.write( line )
newFile.write ( "Each line contains name, average score, individual scores\n" )
line = oldFile.readline()
line = oldFile.readline()

while line != "":
    stringItems = line[ : -1 ].split( sep = "," )
    numberOfItems = len( stringItems )

    if numberOfItems > 2:
        name = []
        numbers = []
        name.append( stringItems[ 0 ] )
        name.append( stringItems[ 1 ] )
        scoresTotal = 0
        pos = 2
        while pos < numberOfItems:
            nextScore = int( stringItems[ pos ] )
            numbers.append( nextScore )
            scoresTotal = scoresTotal + nextScore
            pos = pos + 1

        average = scoresTotal / ( numberOfItems - 2 )
        name.append( average )
        name.append( numbers )
        namestr = str( name )
        newFile.write( namestr )
        
    line = oldFile.readline()

newFile.close()
