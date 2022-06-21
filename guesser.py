import random
print("Number guessing game")
number = random.randint(1,9)
chances = 0
print("guess a no.(between 1 and 9):")

while chances < 5:
        guess = int(input("enter your guess:"))

        if guess == number:
            print("u win")
            break
        elif guess < number:
            print("your guess was too low")

        else:
            print("ur guess was too high")

        chances += 1

        if not chances < 5:
         print("you lose!!the number is",number)