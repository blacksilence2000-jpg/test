talents = float(input("enter talents: "))
pounds = float(input("enter pounds: "))
lots = float(input("enter lots: "))

total_grams = (talents * 20 * 32 * 13.3) + (pounds * 32 * 13.3) + (lots * 13.3)

print(f"\nthe weight in modern units: {int(total_grams // 1000)}kgs and {total_grams % 1000:.2f}gs")