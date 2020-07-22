import random
numofguesses = 0

print("Hey There! What is your Name?")
name = input()

number = random.randint(1,20)
print("Number I am thinking of is between 1 and 20" ,name)

while numofguesses < 6:
    print("Take a guess.")
    guess = input()
    guess = int(guess)

    numofguesses = numofguesses + 1
    if guess < number:
        print("Number is too low")
    if guess > number:
        print("Number is too High")
    if guess == number:
        break
if guess == number:
    numofguesses = str(numofguesses)
    print("Well Done!!" ,name , "You guessed the number in:",numofguesses , "tries")

if guess != number:
    number = str(number)
    print("Wrong! The number is",number)