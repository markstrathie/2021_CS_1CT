import turtle
import random
turtle.speed("fastest")

for row in range(5):
    x = random.randint(0,4)
    for col in range(5):
        if col == x :
            turtle.color("red")
        else:
            turtle.color("grey")
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(10)
        turtle.end_fill()
        turtle.penup()
        turtle.forward(20)
        
    turtle.back(100)
    turtle.right(90)
    turtle.forward(20)
    turtle.left(90)
