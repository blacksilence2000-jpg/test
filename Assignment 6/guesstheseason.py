seasons = ("cold", "pretty cold but not as cold", "hot", "chilly")

s = input("enter month number: ").strip()
if s:
    try:
        month = int(s)
    except ValueError:
        month = 0

    if 1 <= month <= 12:
        season = seasons[(month % 12) // 3]
        print(f"month {month} is in {season}.")
    else:
        print("uh did you are a child or something?, write again iwi.")
