weightsFile = open( "weightsData.txt" )

for count in range (4):
    nextPounds = int( weightsFile.readline() )
    
    wholeStones = nextPounds // 14 # // gives whole number
    leftoverPounds = nextPounds % 14 # % gives remainder
    print( wholeStones, "stone", leftoverPounds, "lbs" )

