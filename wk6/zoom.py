f = open( "chat.txt" )
nextLine = f.readline()
persons = {}

while nextLine != "" :
    bits = nextLine.split()
    name = bits[ 2 ] + " " + bits[ 3 ]

    if name not in persons:
        persons[ name ] = 1
    else:
        persons[ name ] = persons[ name ] + 1
        
    nextLine = f.readline()

for x in persons:
    print( "Name: {0}, Chat Entries: {1}".format( x, persons[ x ] ) )
