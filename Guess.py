# This is a guess that number game
import random

guessesTaken = 0

print("What's up, State your name?")
MyName = input()

number = random.randint (1, 20)
print(' well,' + MyName + ' I am thinking of a number between 1 and 20, do you think you can get it?')

while guessesTaken < 6:
    print('Take a guess and try that luck.') #there are four spaces in front of print
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1

    if guess < number:
        print ('your guess is too low, lil fella') #8 spaces on this one

    if guess > number:
        print ('You are too high big fella')

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print('Good job ,'+ MyName + '! You guessed my number in ' + guessesTaken + ' gussees')

if guess != number:
    number = str(number)
    print ('NAH. The number i was thinking of was ' + number + ' better try again or accept failure partna. lol :D')
