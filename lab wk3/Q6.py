f = open( "readings.txt" )

nextLine = f.readline()

while nextLine != "":
    if int( nextLine ) < 0:
        print( "0" )
    else:
        print( int(nextLine) )
    nextLine = f.readline()
