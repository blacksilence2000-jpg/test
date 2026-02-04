def extract_middle(s):
    length = len(s)
    mid = length // 2
    if length % 2 == 1:
        return s[mid]
    else:
        return s[mid - 1:mid + 1]

input = input("enter a string: ")
middle_character = extract_middle(input)
print("middle character(s):", middle_character)