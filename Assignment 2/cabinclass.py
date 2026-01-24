def cabin_class():
    cabin = input("Enter cabin class (LUX, A, B, C): ").upper()
    
    if cabin == "LUX":
        print("yoooo bro rich, go to upper-deck cabin with a balcony please.")
    elif cabin == "A":
        print("yea still middle class, go to above the car deck, equipped with a window please.")
    elif cabin == "B":
        print("No sight for you, windowless cabin above the car deck please.")
    elif cabin == "C":
        print("No sight for you too, windowless cabin above the car deck please.")
    else:
        print("i think you should check it again, invalid cabin class, next")

cabin_class()