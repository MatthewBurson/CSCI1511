import random

class Coin:
    def __init__(self):
        self.__amount = 20
        self.__sideup = None

    def toss(self):
        result = random.randint(0, 1)
        if result == 0:
            self.__sideup = "Heads"
        else:
            self.__sideup = "Tails"

    def get_sideup(self):
        return self.__sideup

    def set_amount(self, change):
        self.__amount += change

    def get_amount(self):
        return self.__amount

    def spend(self):
        self.__amount = random.randint(-10,0)
        if self.__amount == 0:
            print("Your hand gets slapped... just a little humor.")

def main():
    player1_coin = Coin()
    player2_coin = Coin()

    play_again = input("Do you want to play? (y/n): ")

    while play_again.lower() == 'y': # Corrected line: lowercase the input *before* checking
        player1_coin.toss()
        player2_coin.toss()

        player1_side = player1_coin.get_sideup()
        player2_side = player2_coin.get_sideup()

        print(f"Player 1 tossed: {player1_side}")
        print(f"Player 2 tossed: {player2_side}")

        if player1_side == player2_side:
            player1_coin.set_amount(1)
            player2_coin.set_amount(-1)
            print("Coins matched!")
        else:
            player1_coin.set_amount(-1)
            player2_coin.set_amount(1)
            print("Coins did not match.")

        print(f"Player 1 coins: {player1_coin.get_amount()}")
        print(f"Player 2 coins: {player2_coin.get_amount()}")

        play_again = input("Do you want to play again? (y/n): ")

    print("\nGame Over!")
    print(f"Final Player 1 coins: {player1_coin.get_amount()}")
    print(f"Final Player 2 coins: {player2_coin.get_amount()}")

if __name__ == "__main__":
    main()