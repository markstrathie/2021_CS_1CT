import turtle

turtle.shape( "square" )

turtle.penup()
turtle.hideturtle()

# Sets 250 millisecond (1/4 of a second)
# delay between turtle screen updates.
# Hence, slows things down so we can see
turtle.delay( 250 )

stamps = []

# Add 10 stamps/squares, remembering ids in list
for i in range( 10 ):
    stamps.append( turtle.stamp() )
    turtle.forward( 30 )

# Now remove the stamps/squares
for i in stamps:
    turtle.clearstamp( i )

