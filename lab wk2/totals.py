totals = open( "numbers.txt" )

runSoFar = 0
walkSoFar = 0

for dayNumber in range( 10 ):
    todaysRun = int( totals.readline() )
    runSoFar = runSoFar + todaysRun
    todaysWalk = int( totals.readline() )
    walkSoFar = walkSoFar + todaysWalk

print( "Total time ran:", runSoFar, "minutes." )
print( "Total time walked:", walkSoFar, "minutes." )
