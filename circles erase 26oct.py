import turtle
import random
turtle.speed("fastest")
turtle.color("grey")

for row in range(5):
    for col in range(5):
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

coord = input("select a circle: ")
bits = coord.split(sep=",")
col = int(bits[0])
row = int(bits[1])

turtle.forward(col*20)
turtle.left(90)
turtle.forward(row*20+20)
turtle.right(90)
turtle.pendown()
turtle.color("white")
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()
turtle.penup()
turtle.hideturtle()
