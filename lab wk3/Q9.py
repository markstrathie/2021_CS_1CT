filename = input( "Please type in the filename: " ) #Q9
f = open( filename )

exerciseSoFar = 0

for weekNumber in range( 10 ):
    for dayNumber in range( 7 ):
        todaysExercise = int( f.readline() )
        exerciseSoFar = exerciseSoFar + todaysExercise

    weeklyExerciseHours = exerciseSoFar // 60
    weeklyExerciseMinutes = exerciseSoFar % 60
    print( "You have exercised", weeklyExerciseHours, "hours and", weeklyExerciseMinutes, "minutes this week!" )
    exerciseSoFar = 0
