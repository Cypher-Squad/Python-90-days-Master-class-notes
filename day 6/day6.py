#1. basic if- else statement
age = 20
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

    #if elif else statement
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:    
    print("Grade: D")
else:
    print("Grade: F")
   
    print(f"Your grade is: {grade}")

    # Logical operators
temperature = 25
if temperature > 30:
    print("It's hot outside.")  
elif temperature < 10:
    print("It's cold outside.")
else:
    print("The weather is moderate.")

    # Nested conditions
number = 15
if number > 0:
    if number % 2 == 0:
        print("The number is positive and even.")
    else:
        print("The number is positive and odd.")
else:    print("The number is not positive.")
