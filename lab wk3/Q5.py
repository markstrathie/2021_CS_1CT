f = open( "readings.txt" )

nextLine = f.readline()

while nextLine != "":
    if float( nextLine ) > 0:
        print( nextLine )
    nextLine = f.readline()
