import turtle

def drawDot():
    if stillRunning:
        turtle.forward( 1 )
        turtle.ontimer( drawDot, 100 )

def start():
    global stillRunning
    stillRunning = True
    turtle.ontimer( drawDot, 100 )

def stop():
    global stillRunning
    stillRunning = False

def going():
    global stillRunning
    stillRunning = False
    turtle.bye()

def clickCallback( x, y ):
    global stillRunning
    if not stillRunning:
        turtle.ontimer( drawDot, 100 )
    stillRunning = not stillRunning

turtle.onscreenclick( clickCallback )     


turtle.onkeypress( going, "Escape" )
turtle.onkeypress( start, "Right" )
turtle.onkeypress( stop, "Left" )
turtle.listen()

start()

turtle.mainloop()
