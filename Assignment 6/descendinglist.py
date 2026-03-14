numbers = []
while True:
    s = input("enter number: ")
    if s == "":
        break
    try:
        num = float(s)
    except ValueError:
        print("Pls real number.")
        continue
    numbers.append(num)
numbers.sort(reverse=True)

top_five = numbers[:5]

print("\nfive greatest numbers are:")
for n in top_five:
    if n.isinteger():
        print(int(n))
    else:
        print(n)
