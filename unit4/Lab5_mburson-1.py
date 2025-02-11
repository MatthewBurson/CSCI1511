import random
def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2
    print(f"Roll: {die1}, {die2}  Total: {total}")

    if die1 == 1 and die2 == 1:
        print("Term: Snake Eyes")
    elif total == 3:
        print("Term: Ace Caught a Deuce")
    elif die1 == 2 and die2 == 2:
        print("Term: Little Joe from Kokomo")
    elif total == 5:
        print("Term: Little Phoebe")
    elif die1 == 3 and die2 == 3:
        print("Term: Jimmy Hicks from the Sticks")
    elif die1 == 6 and die2 == 1:
        print("Term: Six Ace")
    elif die1 == 4 and die2 == 4:
        print("Term: Eighter from Decatur")
    elif total == 9:
        print("Term: Nina from Pasadena")
    elif die1 == 5 and die2 == 5:
        print("Term: Puppy Paws")
    elif die1 == 6 and die2 == 5:
        print("Term: Six Five no Jive")
    elif total == 12:
        print("Term: oxcars")
    else:
        print("Term: No term for this roll.")


while True:
    roll_dice()
    again = input("Roll again? (yes/no): ")
    if again != "yes":
        break

    print("thanks for playing!")