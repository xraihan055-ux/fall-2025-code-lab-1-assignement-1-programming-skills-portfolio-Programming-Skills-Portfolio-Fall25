# ... password code...
correct_password = "12345"

while True:
    attempt = input("Enter the password: ").strip()
    if attempt == correct_password:
        print("Access granted. Password correct.")
        break
    else:
        print("Incorrect password. Try again.")
