#Number Guessing Game
#Code inspired by https://inventwithpython.com/chapter4.html

import random

guessesTaken = 0

print('Hello. Who are you?')
myName = raw_input()

number = random.randint(0, 15)
#Possible answers range from 0 to 15

print('I am thinking of a number between 0 and 15')

while guessesTaken < 5:
    print('Make your guess.')
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1

#Next lines of code let the player know if they're too high or too low

    if guess < number:
        print('My number is higher than that!')

    if guess > number:
        print('My number is lower than that!')

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print('Nice, ' + myName + '! You got it right in ' + guessesTaken + ' tries!')

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking was ' + number)


