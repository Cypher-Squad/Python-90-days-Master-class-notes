#Build a basic login system with 3 attempts. After 3 wrong attempts, print "Account locked."
#1. Basic login system with 3 attempts
correct_username = "admin"
correct_password = "password123"
attempts = 3
while attempts > 0:
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == correct_username and password == correct_password:
        print("Login successful.")
        break
    else:
        attempts -= 1
        print(f"Invalid username or password. Attempts left: {attempts}")
if attempts == 0:
    print("Account locked.")
    