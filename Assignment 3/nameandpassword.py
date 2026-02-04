
username = "python"
password = "rules"
attempts = 0

while attempts < 5:
    user_input = input("enter username: ")
    pass_input = input("enter password: ")
    if user_input == username and pass_input == password:
        print("you are in")
        break
    else:
        attempts += 1
        if attempts < 5:
            print(f"wrong one bro, hope you dont have dementia. attempts remaining: {5 - attempts}")
        else:
            print("you are not getting in, see ya")