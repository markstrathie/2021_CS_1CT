import turtle
turtle.reset()
turtle.hideturtle()
turtle.begin_fill()
turtle.pendown()
turtle.color("saddle brown")

for border in range(4):
    turtle.forward(160)
    turtle.right(90)

for row in range(8):
    if row % 2 == 0:
        clr1 = "saddle brown"
        clr2 = "beige"
    else:
        clr1 = "beige"
        clr2 = "saddle brown"

    for col in range(8):
        if col % 2 == 0: # even number
            turtle.color(clr1)
        else: # odd number
            turtle.color(clr2)
            
        turtle.begin_fill()
        turtle.pendown()
        
        for side in range(4):
            turtle.forward(20)
            turtle.right(90)
            
        turtle.end_fill()
        turtle.penup()
        turtle.forward(20)
        
    turtle.back(160)
    turtle.right(90)
    turtle.forward(20)
    turtle.left(90)
