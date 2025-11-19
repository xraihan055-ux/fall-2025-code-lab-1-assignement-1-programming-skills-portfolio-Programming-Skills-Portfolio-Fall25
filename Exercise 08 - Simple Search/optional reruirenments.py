
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

query = input("Enter name to search for: ").strip()
query_lower = query.lower()
names_lower = [n.lower() for n in names]

if query_lower in names_lower:
    idx = names_lower.index(query_lower)
    print(f"{names[idx]} found at index {idx}.")
else:
    print(f"{query} not found.")