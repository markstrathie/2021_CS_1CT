f = open( "readings.txt" )
total = 0
numbersRead = 0

while total < 100:
    total = total + int( f.readline() )
    numbersRead = numbersRead + 1

print( total )
print( numbersRead )
