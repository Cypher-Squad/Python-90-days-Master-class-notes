name = "Raaz"
email = "devlopeda@gmail.com"

#basic operations
print (len(name))
print(name.upper())
print(name.lower())
print(name.replace("Raaz", "Asif"))

#slicing

print(name[0:4])
print(name[-6:])

# f-string (most use in real code)

age = 25
message = f"my name is {name} , and i am {age} years old."
print(message)

#check if substrting exists

print("Raaz" in name)
print("@" in email)

#split a string

words = name.split(" ")
print(words)
