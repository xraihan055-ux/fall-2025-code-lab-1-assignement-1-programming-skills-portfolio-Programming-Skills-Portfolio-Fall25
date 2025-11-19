month_days = {
    1: 31, 2: 28, 3: 31, 4: 30,
    5: 31, 6: 30, 7: 31, 8: 31,
    9: 30, 10: 31, 11: 30, 12: 31
}

try:
    month = int(input("Enter month number (1-12): ").strip())
except ValueError:
    print("Invalid input. Please enter an integer between 1 and 12.")
else:
    if 1 <= month <= 12:
        print(f"Month {month} has {month_days[month]} days.")
    else:
        print("Invalid month number. Please enter a number between 1 and 12.")
