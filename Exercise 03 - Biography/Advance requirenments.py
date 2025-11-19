# Get user input (handles multi-word names/hometowns)
name = input("Enter your full name: ").strip()
hometown = input("Enter your hometown: ").strip()

# Validate age input to ensure it's an integer
while True:
    age_input = input("Enter your age (integer): ").strip()
    try:
        age = int(age_input)
        break
    except ValueError:
        print("Invalid age. Please enter a whole number (e.g., 20).")

person = {
    "name": name,
    "hometown": hometown,
    "age": age
}
