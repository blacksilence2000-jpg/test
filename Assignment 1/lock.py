import random
threedigits = [random.randint(0, 9) for int in range(3)]
fourdigits = [random.randint(1, 6) for int in range(4)]

print(f"3-digit combination: {' '.join(map(str, threedigits))}")
print(f"4-digit combination: {' '.join(map(str, fourdigits))}")