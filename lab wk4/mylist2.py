myList =  [ 3, 7, -1, 2, -10, 6, 8 ]
newList = []
pos = 0

while pos <= 6:
    number = myList[ pos ]
    if number >= 0:
        newList.append( number )
    else:
        newList.append( 0 )
    pos = pos + 1

print( newList )

