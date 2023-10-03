import turtle
rad = 100
colours = ['red', 'orange', 'yellow', 'green',
           'blue', 'purple', 'pink', 'white']

for c in range(8):
    turtle.color(colours[c])
    turtle.left(90)
    turtle.begin_fill()
    turtle.pendown()
    turtle.circle(rad, 180)
    turtle.end_fill()
    turtle.penup()
    turtle.left(90)
    turtle.forward(rad * 2 - 5)
    rad = rad - 5

turtle.hideturtle()
