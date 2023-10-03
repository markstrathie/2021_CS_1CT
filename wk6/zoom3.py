f = open( "chat.txt" )
nextLine = f.readline()
persons = {}

while nextLine != "" :
    name = nextLine.split()[ 2 ] + " " + nextLine.split()[ 3 ]
    msg = nextLine.split( sep = ":" )[ 3 ][ 1:-1 ]

    if name not in persons:
        persons[ name ] = [msg]
    else:
        persons[name].append(msg)
        
    nextLine = f.readline()

i = 0
while i == 0 :
    username = input( "Please type in person's name: " )
    
    if username in persons:
        for x in persons[username]:
            print( x )
    else:
        print("No posts from this person.")

    print()
