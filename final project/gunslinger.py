import turtle
import random

#set counters, 'stats'
score = 0
ammo = 6
health = 2
gameRunning = True

#set turtle background
win = turtle.Screen()
win.bgpic( "background.gif" )

#set turtle cursor
turtle.penup()
turtle.setpos( 0, -100 )
win.register_shape( "klaus.gif" )
win.register_shape( "klaus1.gif" )
turtle.shape( "klaus.gif" )

#setting up turtle movement when 'hit'
def moveEnemy():
    if gameRunning == True:
        x = random.randint( 0, 650 )
        turtle.setpos( x, -100 )
        turtle.showturtle()

#setting up click-to-shoot
def clickResponse( x, y ):
    global score
    global ammo
    global health
    global gameRunning
    if gameRunning == True:
        #checking if player has 'ammo' in 'gun'
        if ammo != 0:
            ammo = ammo - 1
            enemyPos = turtle.pos()
            #if player 'shoots' enemy
            if x > enemyPos[0]-35 and x < enemyPos[0]+35 and y > enemyPos[1]-60 and y < enemyPos[0]+60:
                score = score + 1
                #if player scores 19 'hits' then they win the game
                if score == 20:
                    turtle.color( "dark green" )
                    turtle.write( "YOU\nWIN", font=( "Arial", 20, "bold" ) )
                    gameRunning = False
                turtle.hideturtle()
                moveEnemy()
        #if player 'shoots' with no ammo, giving enemy time to shoot player
        else:
            health = health - 1
            win.bgpic( "background1.gif" )
            turtle.shape( "klaus1.gif" )
            if health == 0:
                turtle.color( "dark red" )
                turtle.write( "GAME\nOVER", font=( "Arial", 20, "bold" ) )
                gameRunning = False

#pressing 's' shows stats in python shell
def stats():
    print( "Your score is {0}/20.\nYour health is {1}/2.\nYour ammo is {2}/6.\n".format( score, health, ammo ) )

#setting 'reload' function to reset ammo counter and images
def reload():
    if gameRunning == True:
        global ammo
        ammo = 6
        win.bgpic( "background.gif" )
        turtle.shape( "klaus.gif" )

#showing player instructions in python shell
print( "Instructions:\nShoot Loco 20 times to kill him and win the game. But be careful!\nHe will move around to avoid your shots.\nIt's best to maximise the turtle window so you can find him.\nYou have 6 bullets in your gun. Make sure you keep it loaded.\nIf you run out of ammo you'll give Loco time to shoot back!\nHe is a deadly gunslinger at can kill you in 2 shots!! Good luck.\n\nControls:\nUse your mouse cursor to aim and left-click to shoot.\nPress 's' to show your score, health and ammo here in the python shell.\nPress 'r' to reload 6 bullets in your gun.\nPress 'Esc' to quit.\n" )

#callback functions
turtle.onscreenclick( clickResponse )
turtle.onkeypress( turtle.bye, "Escape" )
turtle.onkeypress( stats, "s" )
turtle.onkeypress( reload, "r" )

turtle.listen()
turtle.mainloop()
    
