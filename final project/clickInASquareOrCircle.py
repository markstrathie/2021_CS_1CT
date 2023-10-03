import turtle
import math

def circle():
    turtle.setpos( 70, 50 )
    turtle.pendown()
    turtle.circle( 20 )
    turtle.penup()

def square( x, y ):
    turtle.penup()
    turtle.setpos( x, y )
    turtle.setheading( 0 )
    turtle.pendown()
    for i in range( 4 ):
        turtle.forward( 40 )
        turtle.left( 90 )
    turtle.penup()

square( 10,10 )
circle()

def clickResponse( x, y ):
    if x > 0 and x < 40 and y > 0 and y < 40:
        print( "Lower left" )
    elif math.sqrt( (x-70)**2 + (y-70)**2 ) <= 20:
        print( "Circle" )
    else:
        print( "Not in a box" )

turtle.onscreenclick( clickResponse )
turtle.onkeypress( turtle.bye, "Return" )
turtle.listen()

turtle.mainloop()

