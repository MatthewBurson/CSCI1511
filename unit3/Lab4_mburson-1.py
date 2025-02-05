import random

while True:
    
    num_cards = int(input("Please enter number of cards in hand (or 0 to end): "))
    if num_cards == 0:
        break
    card_values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    suits = ["c", "h", "s", "d"]

    print("Your hand:")
    for _ in range(num_cards):
        card_value = random.choice(card_values)
        suit = random.choice(suits)
        print(card_value + suit, end=", ")
    print()
print("Thanks for playing!")
