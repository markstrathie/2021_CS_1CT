# A program to be used in the Familiarisation Lab
# Quintin

data = open( "meaurements.txt" )

length = int( data.readline() )
width = int( data.readline() )
crosssectionwidth = int( data.readline() )

lengthNeeded = ( (2 * length )+(2*(width-(2*crosssectionwidth))))

print( "you need", lengthNeeded, "mm of wood")

