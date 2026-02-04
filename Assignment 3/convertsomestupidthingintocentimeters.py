def inches_to_centimeters(inches):
    return inches * 2.54
def main():
    while True:
        try:
            inches = float(input("enter inches: "))
            if inches < 0:
                break
            print(f"{inches} inches is {inches_to_centimeters(inches):.2f} centimeters.")
        except ValueError:
            print("real number pls😭.")
if __name__ == "__main__":
    main()
#pls dont judge this file name, i just hate ameriencan units