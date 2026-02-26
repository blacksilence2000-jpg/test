#i have read your comments in Assignment 2 and i really appreciate about it, thank you for your materials and i really have fun learning with it. 
def main():
    numbers = set()
    while True:
        user_input = input("enter a number (or press Enter to quit): ")
        if user_input == "":
            break
        try:
            number = float(user_input)
            numbers.add(number)
        except ValueError:
            print("valid number pls.")
    sorted_numbers = sorted(numbers, reverse=True)
    top_five = sorted_numbers[:5]
    print("these are top 5 GREASTEST numbers:", top_five)

if __name__ == "__main__":
    main()
