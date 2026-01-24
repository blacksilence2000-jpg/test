import math

def calculate_unit_price(diameter_cm, price_usd):
    radius_cm = diameter_cm / 2
    area_cm2 = math.pi * radius_cm ** 2
    area_m2 = area_cm2 / 10000
    unit_price_cm2 = price_usd / area_cm2
    unit_price_m2 = price_usd / area_m2
    return unit_price_cm2, unit_price_m2

def main():
    print("pizza value comparer")
    print("-" * 40)
    diameter1 = float(input("enter diameter of pizza 1 (cm): "))
    price1 = float(input("enter price of pizza 1 (USD): "))
    unit_price1_cm2, unit_price1_m2 = calculate_unit_price(diameter1, price1)
    
    diameter2 = float(input("enter diameter of pizza 2 (cm): "))
    price2 = float(input("enter price of pizza 2 (USD): "))
    unit_price2_cm2, unit_price2_m2 = calculate_unit_price(diameter2, price2)
    
    print("\n" + "-" * 40)
    print(f"pizza 1 unit price: ${unit_price1_cm2:.2f}/cm^2 or ${unit_price1_m2:.2f}/m^2")
    print(f"pizza 2 unit price: ${unit_price2_cm2:.2f}/cm^2 or ${unit_price2_m2:.2f}/m^2")
    print("-" * 40)
    
    if unit_price1_cm2 < unit_price2_cm2:
        print("pizza 1 definitely worth it")
    elif unit_price2_cm2 < unit_price1_cm2:
        print("pizza 2 definitely worth it")
    else:
        print("both pizzas have the same unit price, buy both if you want")

if __name__ == "__main__":
    main()
#i think provide both the unit price per cm^2 and m^2 would be better