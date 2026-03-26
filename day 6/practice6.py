# #🏋️ Practice Exercises
# Check if a number is positive, negative, or zero.
# Given an age, print if the person can vote (18+) or not.
# Check if a username and password match hardcoded values.
# Print if a number is even or odd.
# Given a temperature, print "Hot" (>35), "Warm" (20-35), or "Cold" (<20).

#1. Check if a number is positive, negative, or zero.
number = float(input("Enter a number: "))
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
#2. Given an age, print if the person can vote (18+) or not.
age = int(input("Enter your age: "))
if age >= 18:
    print("You can vote.")
else:
    print("You cannot vote.")
#3. Check if a username and password match hardcoded values.
username = input("Enter username: ")
password = input("Enter password: ")
if username == "admin" and password == "password123":
    print("Login successful.")
else:
    print("Invalid username or password.")
#4. Print if a number is even or odd.
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
#5. Given a temperature, print "Hot" (>35), "Warm" (20
-35), or "Cold" (<20).
temperature = float(input("Enter the temperature: "))
if temperature > 35:
    print("Hot")
elif temperature >= 20:
    print("Warm")
else:
    print("Cold")
    