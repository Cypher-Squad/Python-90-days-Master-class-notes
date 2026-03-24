# string 
text = "hello world"
clean_text = text.strip()
print(clean_text)

# email checking
email = "raazalam@gmail.com"
if "@" in email in email:
    print("valid email")
else:
    print("invalid email")

    #full name characters count

first_name = "Raaz alam"
print(len(first_name))

# split fruits names
fruits = "apple,banana,cherry"
result = fruits.split(",")
print(result)

# f-string introduction
name = "Raaz"
age = 17       
city = "Patna"
intro = f"My name is {name}, I am {age} years old and I live in {city}."
print(intro)
