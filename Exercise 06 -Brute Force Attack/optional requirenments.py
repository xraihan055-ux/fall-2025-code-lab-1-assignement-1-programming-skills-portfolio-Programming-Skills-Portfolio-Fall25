# . password  attempt code with limited tries
correct_password = "12345"
max_attempts = 5
attempts = 0

while attempts < max_attempts:
    attempt = input("Enter the password: ").strip()
    if attempt == correct_password:
        print("Access granted. Password correct.")
        break
    attempts += 1
    remaining = max_attempts - attempts
    if remaining > 0:
        print(f"Incorrect password. {remaining} attempts remaining.")
    else:
        print("Maximum attempts reached. Authorities have been alerted.")
