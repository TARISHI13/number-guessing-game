import random
number = random.randint(1,9)
chances = 5
print("guess a number between 1 to 9")
while chances > 0 : 
    guess = int(input("enter your guess"))
    if guess == number : 
        print("u have guessed a correct number")
        break
    elif guess > number : 
        print("your guess is too high, guess a ower number")

    else : 
        print("your guess was too low, guess a higher number")

    chances -= 1

if chances == 0 :
    print("you have lost")