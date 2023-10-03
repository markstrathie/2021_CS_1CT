f = open( "chat.txt" )
nextLine = f.readline()
persons = {}

while nextLine != "" :
    bits = nextLine.split()
    name = bits[ 2 ] + " " + bits[ 3 ]
    msg = nextLine.split(sep = ":")[3][1:-1]

    if name not in persons:
        persons[ name ] = [msg]
    else:
        persons[name].append(msg)
        
    nextLine = f.readline()

for x in persons:
    print( "Name: {0}\nChats:".format( x ),end=" " )
    for y in persons[x]:
        print( "{0}\n".format( y ),end="" )
    print("\n",end="")
