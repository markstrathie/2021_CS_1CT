import random
x = random.randint(1,10)
tries = 0
guess = input("I'm thinking of a number between 1 and 100. Type in your guess: ")
guessInt = int(guess)

while guessInt != x :
    tries = tries + 1
    guess = input("Ha ha! That's wrong. Try again: ")
    guessInt = int(guess)

print("Congratulations, you beat me! It took you %d tries. See if you can do better next time!"%(tries+1))
