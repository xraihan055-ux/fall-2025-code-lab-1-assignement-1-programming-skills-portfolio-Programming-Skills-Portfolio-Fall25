# ...simple search code
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]
target = "Sam"

if target in names:
    print(f"{target} found at index {names.index(target)}.")
else:
    print(f"{target} not found.")
