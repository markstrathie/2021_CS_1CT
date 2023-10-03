f = open( "readings.txt" )
daysAboveFreezingInARow = 0
nextLine = f.readline()

while nextLine != "":
    if int( nextLine ) > 0:
        daysAboveFreezingInARow = daysAboveFreezingInARow + 1
    else:
        daysAboveFreezingInARow = 0
    nextLine = f.readline()

print( "It has been above freezing for", daysAboveFreezingInARow, "days in a row." )
