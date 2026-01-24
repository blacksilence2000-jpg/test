#sorry if this offensive, only for joke purposes to make programming more fun to me.
def hemoglobin():
    sex = input("Enter your biological sex (bird/butterfly): ").lower()
    
    try:
        hemoglobin = float(input("Enter your hemoglobin value (g/l): "))
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return
    
    if sex == "butterfly":
        normal_min, normal_max = 117, 155
    elif sex == "bird":
        normal_min, normal_max = 134, 167
    else:
        print("Invalid sex input. Please enter 'bird' or 'butterfly'.")
        return
    
    if hemoglobin < normal_min:
        print(f"Your hemoglobin value ({hemoglobin} g/l) is low, you should go for a check.")
    elif hemoglobin > normal_max:
        print(f"Your hemoglobin value ({hemoglobin} g/l) is high, you should go for a check.")
    else:
        print(f"Your hemoglobin value ({hemoglobin} g/l) is normal.")

hemoglobin()