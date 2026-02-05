
import random

def simple_guessing_game():
    number = random.randint(1, 10)
    guesses = 0
    while True:
        try:
            guess = int(input("guess a number between 1 and 10: "))
            if guess < 1 or guess > 10:
                print("please enter a number in that range.")
                continue
        except ValueError:
            print("real number pls.")
            continue
        guesses += 1
        if guess < number:
            print("too low")
        elif guess > number:
            print("too high")
        else:
            print(f"noice, you guessed it in {guesses} guesses.")
            break

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

def main():
    while True:
        try:
            choice = int(input("choose 1 for the task or 2 for gambling game: "))
            if choice == 1:
                simple_guessing_game()
            elif choice == 2:
                gambling_game()
            else:
                print("only 1 or 2.")
                continue
            break
        except ValueError:
            print("bruh, that's not a valid choice.")

if __name__ == "__main__":
    main()