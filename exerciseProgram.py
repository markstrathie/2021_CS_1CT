filename = input( "Please type in the filename: " )
exerciseFile = open( filename)

exerciseSoFar = 0
numberOfValuesInFile = int( exerciseFile.readline() )

for dayNumber in range( numberOfValuesInFile ):
    todaysExercise = int( exerciseFile.readline() )
    exerciseSoFar = exerciseSoFar + todaysExercise

exerciseHours = exerciseSoFar // 60
exerciseMinutes = exerciseSoFar % 60

print( "You have exercised", exerciseHours, "hours and", exerciseMinutes, "minutes this month!" )
