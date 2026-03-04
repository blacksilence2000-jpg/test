import re
def findtosum(text):
    numbers = re.findall(r"\d+", text)
    total = 0

    for n in numbers:
        total = total + int(n)
    return total
