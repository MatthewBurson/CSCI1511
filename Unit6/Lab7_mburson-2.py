import random

ran_num = random.randint(1, 100)
guesses = 0
guess = None

print("Welcome to guess my Number!")
print("I am generating random number.")

while guess != ran_num: 
        guess = int(input("Enter your guess: "))
        guesses += 1

        if guess < ran_num: 
            print("Too low! Try again.")
        elif guess > ran_num:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {guesses} guesses!")
            break