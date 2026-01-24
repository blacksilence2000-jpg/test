def zander_size():
    size_limit = 42
    length = float(input("enter the length of the zander in centimeters: "))
    
    if length < size_limit:
        difference = size_limit - length
        print(f"the fish is free. The zander is {difference} cm below the size limit.")
    else:
        print("yay, keep the fish bro, goodjob.")

zander_size()