myString = "Here is the data you need: 3, 4, 8, 1, 3\n"
numbers = myString[ 27 : -1 ]
onlyNumbers = numbers.split( sep = "," )
newList = []
pos = 0

while pos <= 4:
    number = int( onlyNumbers[ pos ] )
    newList.append( number )
    pos = pos + 1

print( newList )
