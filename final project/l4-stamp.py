import turtle

turtle.shape( "square" )

lastStamp = turtle.stamp()
turtle.hideturtle()
turtle.penup()

def rightResponse():
    global lastStamp
    turtle.clearstamp( lastStamp )
    turtle.forward( 10 )
    lastStamp = turtle.stamp()

def leftResponse():
    global lastStamp
    turtle.clearstamp( lastStamp )
    turtle.forward( -10 )
    lastStamp = turtle.stamp()

turtle.onkeypress( rightResponse, "Right" )
turtle.onkeypress( leftResponse, "Left" )

turtle.onkeypress( turtle.bye, "Escape" )

turtle.listen()
turtle.mainloop()
