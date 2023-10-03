#\u250c top left
#\u2510 top right
#\u2514 bottom left
#\u2518 bottom right
#\u2500 horizontal
#\u2502 vertical

width = input( "Please type in character width of box: " )
boxSize = int( width )

print( "\u250c" + "\u2500" * boxSize + "\u2510" )

for size in range( boxSize ):
    print( "\u2502" + " " * boxSize + "\u2502" )
    
print( "\u2514" + "\u2500" * boxSize + "\u2518" )
