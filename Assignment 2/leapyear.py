def check_leap_year():
    year = int(input("enter a year: "))
    
    if year % 400 == 0:
        print(f"{year} is a leap year.")
    elif year % 100 == 0:
        print(f"{year} is not a leap year.")
    elif year % 4 == 0:
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")

check_leap_year()
#yea this have not thing to do with