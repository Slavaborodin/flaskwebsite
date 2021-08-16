import random

username_input=input("Hello, what is your name?  ")

guesses=0
number= random.randint(1,10)

print ("Hi" ,username_input, " I am guessing a number between 1 and 10:")

while guesses < 5:
    guess=int(input())
    guesses +=1

    if guess < number:
        print ("Sorry, your guess is too low, try again ")

    if guess > number:
        print ("Sorry, your guess is too high, try again")

    if guess == number:
        break

if guess==number:
    print ("You have guessed the number in " , str(guesses) , "tries")

else:
    print ("You couldn't get the number, the number was: ", str(number))


