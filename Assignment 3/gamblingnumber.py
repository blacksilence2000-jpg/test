#i have make it into a gambling game instead of just a number guessing game, hope you still mark it😭

import random

def gambling_game():
    while True:
        try:
            coins = int(input("how many coins do you want to bet with?: "))
            if coins <= 0:
                print("man, you must feed the house to make it work.")
                continue
            break
        except ValueError:
            print("bruh, that not gonna work.")
    while coins > 0:
        print(f"\nyou have {coins} coins.")
        while True:
            try:
                bet = int(input("How many coins do you want to bet? "))
                if bet <= 0 or bet > coins:
                    print("you cant do that, pls feed the house😭.")
                    continue
                break
            except ValueError:
                print("bruh, that not gonna work too.")
        bet_number = random.randint(1, 100)
        guesses = 0
        while True:
            try:
                guess = int(input("Guess a number between 1 and 100: "))
                if guess < 1 or guess > 100:
                    print("Please enter a number between 1 and 100.")
                    continue
            except ValueError:
                print("again, how many time I have told you before, Im not paying enough for this.")
                continue
            guesses += 1
            if guess < bet_number:
                print("too low")
            elif guess > bet_number:
                print("too high")
            else:
                print("what a call man!")
                coins += bet
                print(f"you won {bet} coins!")
                break
        coins -= (guesses - 1)
        print(f"guesses cost: {guesses - 1} coins. coins: {coins}")
    print("\nhaha thank you for feeding the house, see you again next time.")

if __name__ == "__main__":
    gambling_game()