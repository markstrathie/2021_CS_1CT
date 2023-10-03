import turtle

f = open( "drawing.txt" )

drawing = []
count = 0 #Q4

nextLine = f.readline()
while nextLine != "":
    bits = nextLine[ : - 1 ].split( "," )
    if len( bits ) < 5: #Q6 - add colour
        bits.append( "black" ) #Q6
    newLine = { "x": int( bits[ 0 ] ), "y": int( bits[ 1 ] ), "direction": int( bits[ 2 ] ), "len": int( bits[ 3 ] ), "colour": ( bits[ 4 ] ) } #Q6
    drawing.append( newLine )
    
    nextLine = f.readline()

nextInput = input( "Enter (d)raw, (l)ist lines, (c)hange a line, (a)dd new line, (q)uit: " ) #Q5

while nextInput != "q":
    if nextInput == "d":
        for aardvark in drawing:
            turtle.penup()
            turtle.goto( aardvark[ "x" ], aardvark[ "y" ] )
            turtle.color( aardvark[ "colour" ] ) #Q6
            turtle.pendown()
            turtle.setheading( aardvark[ "direction" ] )
            turtle.forward( aardvark[ "len" ] )
        turtle.exitonclick()
    elif nextInput == "l":
        for line in drawing: #Q4 - add line numbers
            print( "{0}. ({1},{2}), direction {3}, length {4}, colour {5}".format( count,line["x"],line["y"],line["direction"],line["len"],line["colour"] ) ) #Q4, #Q6
            count = count + 1 #Q4
        count = 0 #Q4
    elif nextInput == "c":
        lineNum = int( input( "Which line? start from zero" ) )
        newLine = input( "Type in the four numbers for the changed line (and optional colour), separated by spaces" ) #Q6
        bits = newLine.split()
        if len( bits ) < 5: #Q6
            bits.append( "black" ) #Q6
        newPart = { "x": int( bits[ 0 ] ), "y": int( bits[ 1 ] ), "direction": int( bits[ 2 ] ), "len": int( bits[ 3 ] ), "colour": ( bits[ 4 ] ) } #Q6
        drawing[ lineNum ] = newPart
    elif nextInput == "a": #Q5 - add new line
        newLine = input( "Type in the four numbers for the new line (and optional colour), separated by spaces " ) #Q6
        bits = newLine.split()
        if len( bits ) < 5: #Q6
            bits.append( "black" ) #Q6
        newPart = { "x": int( bits[ 0 ] ), "y": int( bits[ 1 ] ), "direction": int( bits[ 2 ] ), "len": int( bits[ 3 ] ), "colour": ( bits[ 4 ] ) } #Q6
        drawing.append( newPart )
    else:
        print( "input not understood" )
    nextInput = input( "What now? " )
