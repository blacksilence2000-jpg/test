numbers = []

while True:
    user_input = input("enter a number (dont just press enter when there is nothing): ")
    if user_input == "":
        break
    numbers.append(float(user_input))
if numbers:
    print(f"min: {min(numbers)}")
    print(f"max: {max(numbers)}")
else:
    print("there is nothing there, what you want me to do with that.")