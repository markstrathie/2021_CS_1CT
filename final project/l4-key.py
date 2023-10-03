import turtle

def keyResponse():
    print( "key pressed" )

turtle.onkeypress( keyResponse, "a" )
turtle.listen()
turtle.mainloop()
