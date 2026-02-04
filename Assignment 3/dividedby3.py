num = 3
count = 0
while num <= 1000:
    print(num, end=" ")
    count += 1
    if count % 24 == 0:
        print()
    num += 3