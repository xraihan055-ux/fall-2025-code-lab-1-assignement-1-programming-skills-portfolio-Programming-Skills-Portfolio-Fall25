
def is_even(n):
    return n % 2 == 0

def main():
    try:
        num = int(input("Enter an integer: ").strip())
    except ValueError:
        print("Invalid input. Please enter a whole number.")
        return

    if is_even(num):
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")

if __name__ == "__main__":
    main()
