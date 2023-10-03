oldFile = open( "people.txt" )
newFile = open( "olderPeople.txt", "w" )

line = oldFile.readline()

while line != "":
    lineSplit = line.split( sep = "," )
    name = lineSplit[ 0 ]
    age = int( lineSplit[ 1 ] )
    if age >= 65:
        newFile.write( name )
        newFile.write ( "\n" )
    line = oldFile.readline()

newFile.close()
