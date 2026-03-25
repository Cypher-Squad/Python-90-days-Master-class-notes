user = {
    "name": "Alice",
    "age": 30,
    "email": "alice@example.com",
    "is_active": True
}

#1. access values
print(user["name"])  # Output: Alice
print(user.get("email"))  # Output: alice@example.com

#2. add a new key

user["city"] = "New York"

#3. update a value 
user["age"] = 31

#4. delete a key
del user["is_active"]

#5. loop through key value pairs
for key, value in user.items():
    print(f"{key}: {value}")

    #6. check if a key exists
if "email" in user:
    print("Email exists in the dictionary.")

    #7. nested dictionary (used apis)
    product = {
        "name": "Laptop",
        "specs": {
            "processor": "Intel i7",
            "ram": "16GB",
            "storage": "512GB SSD"
        }
    }

print(product["specs"]["ram"])  # Output: 16GB
