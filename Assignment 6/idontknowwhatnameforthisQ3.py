seen = set()
while True:
    name = input("enter name: ").strip()
    if name == "":
        break
    if name in seen:
        print("already have that")
    else:
        print("new name")
        seen.add(name)
print("\pnames entered:")
for n in seen:
    print(n)
