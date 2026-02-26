def main():
    cities = []
    for i in range(5):
        city = input(f"enter the name of city: ")
        cities.append(city)
    print("\nthe cities you entered are:")
    for city in cities:
        print(city)

if __name__ == "__main__":
    main()
    