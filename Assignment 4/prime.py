n = int(input("enter an integer to find if this is prime: "))
if n > 1 and all(n % i for i in range(2, int(n**0.5) + 1)):
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")