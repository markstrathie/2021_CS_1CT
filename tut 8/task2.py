import math 
import turtle 

def house(sidelength): 
    rooflength = math.sqrt( 2 ) * sidelength/2 
    turtle.begin_fill() 
    turtle.forward( sidelength ) 
    turtle.left( 90 ) 
    turtle.forward( sidelength ) 
    turtle.left( 45 ) 
    turtle.forward( rooflength ) 
    turtle.left( 90 ) 
    turtle.forward( rooflength ) 
    turtle.left( 45 ) 
    turtle.forward( sidelength ) 
    turtle.left( 90 ) 
    turtle.end_fill()

def row( n, size ):
    for i in range( n ):
        house( size )
        turtle.forward( size )
