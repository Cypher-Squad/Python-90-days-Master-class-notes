#creating a dictionary for a book (title, author, year, price)
book = {
    "title": "1984",
    "author": "George Orwell",
    "year": 1948,
    "price": 12.99
}

#2. access and printing the author name
print(book["author"])  # Output: George Orwell

#3. adding a genre key to the book dictionary
book["genre"] = "Dystopian"

#4. updating the price by 10% and printing the new price
book["price"] *= 1.10
print(book["price"])  # Output: 14.289

#loop through the dictionary and print all keys and values
for key, value in book.items():
    print(f"{key}: {value}")
    
