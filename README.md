# 🐍 90-Day Python Backend Developer Learning Plan

> **Goal:** Become a job-ready Python Backend Developer in 90 days  
> **Daily Commitment:** 2 hours/day — 30 min theory + 90 min coding  
> **Tools Required:** Python 3.10+, VS Code, Git, Postman, SQLite  

---

## 📋 Table of Contents

- [Overview](#overview)
- [Phase 1 — Python Fundamentals (Day 1–20)](#phase-1--python-fundamentals-day-120)
- [Phase 2 — Backend Fundamentals with Flask (Day 21–45)](#phase-2--backend-fundamentals-with-flask-day-2145)
- [Phase 3 — Databases (Day 46–65)](#phase-3--databases-day-4665)
- [Phase 4 — Real Backend Projects (Day 66–90)](#phase-4--real-backend-projects-day-6690)
- [Final Portfolio Structure](#final-github-portfolio-structure)
- [Skills Learned](#skills-learned)

---

## Overview

| Phase | Days | Topic |
|-------|------|-------|
| 🟢 Phase 1 | Day 01–20 | Python Fundamentals |
| 🔵 Phase 2 | Day 21–45 | Backend with Flask |
| 🟡 Phase 3 | Day 46–65 | Databases & SQL |
| 🔴 Phase 4 | Day 66–90 | Real Projects |

---

# Phase 1 — Python Fundamentals (Day 1–20)

> Build a rock-solid Python base before touching backend frameworks.

---

## Day 1 — Python Setup & Your First Program

### 📖 Concept (30 min)
Python is a beginner-friendly, powerful programming language used for web backends, data science, AI, and automation. Before writing code, you need to set up your environment.

**Steps to install:**
1. Download Python 3.10+ from [python.org](https://python.org)
2. Install VS Code from [code.visualstudio.com](https://code.visualstudio.com)
3. Install Python extension in VS Code
4. Open terminal and verify: `python --version`
5. Install Git from [git-scm.com](https://git-scm.com)

### 💻 Code Example

```python
# Your very first Python program
print("Hello, World!")
print("I am learning Python Backend Development!")

# Python can do math
print(2 + 3)
print(10 * 5)
print(100 / 4)
```

### 🏋️ Practice Exercises

1. Print your full name using `print()`
2. Print today's date as a string
3. Print the result of `999 * 999`
4. Print three lines: your name, city, and hobby
5. Write a comment explaining what `print()` does

### 🎯 Mini Challenge
Create a file called `about_me.py` that prints 5 facts about yourself.

### 📌 GitHub Commit
```
Day 01: Python setup and first hello world program
```

---

## Day 2 — Variables & Data Types

### 📖 Concept (30 min)
Variables are containers that store information. Python has several basic data types:
- `int` — whole numbers like `5`, `100`
- `float` — decimal numbers like `3.14`
- `str` — text wrapped in quotes like `"hello"`
- `bool` — True or False

Python figures out the type automatically — you don't have to declare it!

### 💻 Code Example

```python
# Variables
name = "Arjun"           # string
age = 22                 # integer
gpa = 8.5                # float
is_student = True        # boolean

print(name)
print(age)
print(gpa)
print(is_student)

# Check the type of a variable
print(type(name))        # <class 'str'>
print(type(age))         # <class 'int'>
print(type(gpa))         # <class 'float'>
print(type(is_student))  # <class 'bool'>

# You can change a variable's value
age = 23
print(age)               # 23
```

### 🏋️ Practice Exercises

1. Create variables for your name, age, and city. Print them all.
2. Create a variable `price = 99.99` and print its type.
3. Create a boolean variable `is_employed = False` and print it.
4. Reassign a variable from a number to a string and print both.
5. Use `type()` to check all 4 data types.

### 🎯 Mini Challenge
Create a "student profile" with 6 variables (name, age, course, gpa, city, is_active) and print them with labels.

### 📌 GitHub Commit
```
Day 02: Variables and data types exploration
```

---

## Day 3 — Strings & String Operations

### 📖 Concept (30 min)
Strings are sequences of characters. They are used everywhere in backend development — storing names, messages, API responses, etc.

Key string operations:
- Concatenation (joining): `"Hello" + " World"`
- Length: `len("hello")`
- Slicing: `"hello"[0:3]` → `"hel"`
- Methods: `.upper()`, `.lower()`, `.strip()`, `.replace()`
- f-strings: The modern way to format strings

### 💻 Code Example

```python
name = "Riya Sharma"
email = "riya@example.com"

# Basic operations
print(len(name))             # 11
print(name.upper())          # RIYA SHARMA
print(name.lower())          # riya sharma
print(name.replace("Riya", "Priya"))  # Priya Sharma

# Slicing
print(name[0:4])             # Riya
print(name[-6:])             # Sharma

# f-strings (most used in real code)
age = 25
message = f"My name is {name} and I am {age} years old."
print(message)

# Check if substring exists
print("Riya" in name)        # True
print("@" in email)          # True

# Split a string
words = name.split(" ")
print(words)                 # ['Riya', 'Sharma']
```

### 🏋️ Practice Exercises

1. Take a string `"  hello world  "` and remove spaces using `.strip()`
2. Check if an email contains `"@"` using `in`
3. Count how many characters are in your full name
4. Split the string `"apple,banana,mango"` by comma
5. Create an f-string that introduces you with name, age, and city

### 🎯 Mini Challenge
Write a program that takes a full name like `"john doe"` and converts it to `"John Doe"` using string methods.

### 📌 GitHub Commit
```
Day 03: String operations and f-string formatting
```

---

## Day 4 — Lists

### 📖 Concept (30 min)
A list is an ordered collection of items. Lists can hold any data type and can be changed (mutable).

```
list = [item1, item2, item3]
```

Lists are used constantly in APIs — returning a list of users, products, tasks, etc.

### 💻 Code Example

```python
# Creating lists
fruits = ["apple", "banana", "mango", "orange"]
numbers = [10, 20, 30, 40, 50]
mixed = ["Alice", 25, True, 3.14]

# Access by index (starts at 0)
print(fruits[0])         # apple
print(fruits[-1])        # orange (last item)

# Slicing
print(fruits[1:3])       # ['banana', 'mango']

# List methods
fruits.append("grape")   # Add to end
fruits.remove("banana")  # Remove item
fruits.insert(1, "kiwi") # Insert at index 1
print(len(fruits))       # Length
print(fruits)

# Loop through a list
for fruit in fruits:
    print(fruit)

# List with numbers
scores = [88, 72, 95, 60, 84]
print(max(scores))       # 95
print(min(scores))       # 60
print(sum(scores))       # 399
```

### 🏋️ Practice Exercises

1. Create a list of 5 cities. Print the first and last city.
2. Add a new city to the list and print the updated list.
3. Remove one city and print again.
4. Find the total number of items in a list using `len()`.
5. Loop through a list of names and print `"Hello, {name}!"`

### 🎯 Mini Challenge
Create a shopping cart as a list. Add 3 items, remove 1, and print the final cart with total item count.

### 📌 GitHub Commit
```
Day 04: Python lists and list operations
```

---

## Day 5 — Dictionaries

### 📖 Concept (30 min)
A dictionary stores data as **key-value pairs** — like a real dictionary where each word (key) has a meaning (value). This is the backbone of JSON, which is used in every API.

```python
person = {"name": "Arjun", "age": 22}
```

### 💻 Code Example

```python
# Creating a dictionary
user = {
    "name": "Arjun Singh",
    "age": 22,
    "email": "arjun@example.com",
    "is_active": True
}

# Access values
print(user["name"])          # Arjun Singh
print(user.get("email"))     # arjun@example.com

# Add a new key
user["city"] = "Mumbai"

# Update a value
user["age"] = 23

# Delete a key
del user["is_active"]

# Loop through key-value pairs
for key, value in user.items():
    print(f"{key}: {value}")

# Check if key exists
if "email" in user:
    print("Email found!")

# Nested dictionary (used in APIs!)
product = {
    "id": 1,
    "name": "Laptop",
    "specs": {
        "ram": "16GB",
        "storage": "512GB"
    }
}
print(product["specs"]["ram"])   # 16GB
```

### 🏋️ Practice Exercises

1. Create a dictionary for a book (title, author, year, price).
2. Access and print the author's name.
3. Add a `"genre"` key to the book dictionary.
4. Update the price by 10% and print the new price.
5. Loop through the dictionary and print all keys and values.

### 🎯 Mini Challenge
Build a student report card dictionary with name, marks (as a nested dict with 3 subjects), and calculate the average marks.

### 📌 GitHub Commit
```
Day 05: Dictionaries and key-value data structures
```

---

## Day 6 — Conditions (if/elif/else)

### 📖 Concept (30 min)
Conditions let your program make decisions. Based on whether something is True or False, different code runs.

Comparison operators: `==`, `!=`, `>`, `<`, `>=`, `<=`  
Logical operators: `and`, `or`, `not`

### 💻 Code Example

```python
# Basic if-else
age = 20

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# if-elif-else
score = 75

if score >= 90:
    grade = "A"
elif score >= 75:
    grade = "B"
elif score >= 60:
    grade = "C"
else:
    grade = "F"

print(f"Your grade is: {grade}")

# Logical operators
username = "admin"
password = "1234"

if username == "admin" and password == "1234":
    print("Login successful!")
else:
    print("Invalid credentials.")

# Nested conditions
is_logged_in = True
is_admin = False

if is_logged_in:
    if is_admin:
        print("Welcome, Admin!")
    else:
        print("Welcome, User!")
else:
    print("Please log in.")
```

### 🏋️ Practice Exercises

1. Check if a number is positive, negative, or zero.
2. Given an age, print if the person can vote (18+) or not.
3. Check if a username and password match hardcoded values.
4. Print if a number is even or odd.
5. Given a temperature, print "Hot" (>35), "Warm" (20-35), or "Cold" (<20).

### 🎯 Mini Challenge
Build a basic login system with 3 attempts. After 3 wrong attempts, print "Account locked."

### 📌 GitHub Commit
```
Day 06: Conditional statements and decision making
```

---

## Day 7 — Loops (for & while)

### 📖 Concept (30 min)
Loops repeat code. There are two types:
- `for` loop: Repeat a fixed number of times or over a collection
- `while` loop: Repeat as long as a condition is True

`break` stops the loop early. `continue` skips to the next iteration.

### 💻 Code Example

```python
# for loop — iterate over a list
students = ["Alice", "Bob", "Charlie", "Diana"]

for student in students:
    print(f"Hello, {student}!")

# for loop with range
for i in range(1, 6):
    print(f"Count: {i}")

# while loop
count = 1
while count <= 5:
    print(f"While count: {count}")
    count += 1

# break — stop the loop
for num in range(10):
    if num == 5:
        break
    print(num)

# continue — skip current iteration
for num in range(10):
    if num % 2 == 0:   # skip even numbers
        continue
    print(num)          # prints only odd numbers

# Looping over a dictionary
user = {"name": "Arjun", "age": 22, "city": "Delhi"}
for key, value in user.items():
    print(f"{key} = {value}")
```

### 🏋️ Practice Exercises

1. Print numbers 1 to 20 using a `for` loop.
2. Print all even numbers from 1 to 50.
3. Use a `while` loop to count down from 10 to 1.
4. Loop through a list of fruits and print only those with more than 5 characters.
5. Use `break` to stop a loop when a specific name is found.

### 🎯 Mini Challenge
Write a number guessing game. Generate a fixed number (e.g., 7) and use a `while` loop to keep asking the user to guess until they get it right.

### 📌 GitHub Commit
```
Day 07: For loops, while loops, break and continue
```

---

## Day 8 — Functions

### 📖 Concept (30 min)
Functions are reusable blocks of code. Instead of writing the same code repeatedly, you define it once and call it anywhere.

```python
def function_name(parameters):
    # code
    return result
```

Functions make your code clean, organized, and testable — critical for backend development.

### 💻 Code Example

```python
# Basic function
def greet(name):
    return f"Hello, {name}!"

print(greet("Arjun"))     # Hello, Arjun!
print(greet("Priya"))     # Hello, Priya!

# Function with default parameter
def greet_with_title(name, title="Mr."):
    return f"Hello, {title} {name}!"

print(greet_with_title("Singh"))          # Hello, Mr. Singh!
print(greet_with_title("Sharma", "Dr.")) # Hello, Dr. Sharma!

# Function that returns multiple values
def get_min_max(numbers):
    return min(numbers), max(numbers)

low, high = get_min_max([10, 5, 8, 22, 3])
print(f"Min: {low}, Max: {high}")  # Min: 3, Max: 22

# Function with *args (variable arguments)
def total(*numbers):
    return sum(numbers)

print(total(1, 2, 3))      # 6
print(total(10, 20, 30))   # 60

# Function with **kwargs (keyword arguments)
def create_user(**kwargs):
    return kwargs

user = create_user(name="Alice", age=25, city="Mumbai")
print(user)
```

### 🏋️ Practice Exercises

1. Write a function `add(a, b)` that returns the sum.
2. Write a function `is_even(n)` that returns True if n is even.
3. Write a function `celsius_to_fahrenheit(c)` with the formula `(c * 9/5) + 32`.
4. Write a function `count_vowels(word)` that counts vowels in a string.
5. Write a function `find_largest(lst)` that returns the largest item in a list.

### 🎯 Mini Challenge
Build a mini calculator with 4 functions: `add`, `subtract`, `multiply`, `divide`. Call them based on user input.

### 📌 GitHub Commit
```
Day 08: Functions, return values, and default parameters
```

---

## Day 9 — Error Handling (try/except)

### 📖 Concept (30 min)
Errors happen. A user sends bad data, a file doesn't exist, a network fails. Error handling prevents your program from crashing. Instead of crashing, you **catch** the error and handle it gracefully.

This is extremely important in API development.

### 💻 Code Example

```python
# Basic try-except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

# Catching different error types
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except TypeError:
        return "Invalid types provided"

print(safe_divide(10, 2))    # 5.0
print(safe_divide(10, 0))    # Cannot divide by zero
print(safe_divide(10, "a"))  # Invalid types provided

# try-except-else-finally
def read_number(text):
    try:
        number = int(text)
    except ValueError:
        print("Not a valid number!")
        return None
    else:
        print(f"Successfully parsed: {number}")
        return number
    finally:
        print("Parsing attempt complete.")

read_number("42")
read_number("abc")

# Raising custom errors
def get_user_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    if age > 150:
        raise ValueError("Age seems unrealistic!")
    return age

try:
    print(get_user_age(-5))
except ValueError as e:
    print(f"Error: {e}")
```

### 🏋️ Practice Exercises

1. Write a function that safely converts a string to an integer (return 0 on error).
2. Handle `FileNotFoundError` when trying to open a file that doesn't exist.
3. Write a function that divides two numbers and handles all errors.
4. Create a function that raises a `ValueError` if a username is shorter than 3 characters.
5. Use `finally` to print "Done" no matter what happens.

### 🎯 Mini Challenge
Build a safe input validator for an age field: must be a number, must be between 1 and 120, and must return helpful error messages.

### 📌 GitHub Commit
```
Day 09: Error handling with try-except-finally
```

---

## Day 10 — File Handling

### 📖 Concept (30 min)
File handling lets you read from and write to files. In backend development, you often read config files, write logs, or process uploaded files.

Modes:
- `"r"` — read
- `"w"` — write (overwrites)
- `"a"` — append
- `"r+"` — read and write

Always use `with open(...)` — it automatically closes the file.

### 💻 Code Example

```python
# Writing to a file
with open("notes.txt", "w") as f:
    f.write("Day 10: Learning file handling\n")
    f.write("Python is awesome!\n")

# Reading a file
with open("notes.txt", "r") as f:
    content = f.read()
    print(content)

# Reading line by line
with open("notes.txt", "r") as f:
    for line in f:
        print(line.strip())

# Appending to a file
with open("notes.txt", "a") as f:
    f.write("This line was appended.\n")

# Writing and reading JSON files
import json

user_data = {
    "name": "Arjun",
    "age": 22,
    "skills": ["Python", "Flask", "SQL"]
}

# Write JSON
with open("user.json", "w") as f:
    json.dump(user_data, f, indent=4)

# Read JSON
with open("user.json", "r") as f:
    loaded = json.load(f)
    print(loaded["name"])
    print(loaded["skills"])
```

### 🏋️ Practice Exercises

1. Create a text file and write 3 lines to it.
2. Read the file and print each line with its line number.
3. Append 2 more lines to the file.
4. Write a list of names to a JSON file.
5. Read the JSON file and print only the names.

### 🎯 Mini Challenge
Build a simple "note taking" program that appends each note to a `notes.txt` file with a timestamp.

### 📌 GitHub Commit
```
Day 10: File handling — read, write, append, JSON files
```

---

## Day 11 — Modules & Imports

### 📖 Concept (30 min)
A module is a file containing Python code. You can import built-in modules (like `os`, `math`, `random`) or install third-party ones using `pip`.

This is how you reuse code across files in a real project.

### 💻 Code Example

```python
# Built-in modules
import math
import random
import os
import datetime

print(math.sqrt(144))           # 12.0
print(math.pi)                  # 3.14159...
print(random.randint(1, 100))   # random number
print(os.getcwd())              # current directory

# datetime module (very common in APIs)
now = datetime.datetime.now()
print(now)
print(now.strftime("%Y-%m-%d %H:%M:%S"))

# Import specific function
from math import ceil, floor
print(ceil(4.2))    # 5
print(floor(4.8))   # 4

# Create your own module
# Save this as utils.py:
# def add(a, b):
#     return a + b
#
# def greet(name):
#     return f"Hello, {name}!"

# Then in another file:
# import utils
# print(utils.add(3, 4))
# print(utils.greet("Arjun"))

# Install a third-party module
# In terminal: pip install requests
import requests   # After installing

response = requests.get("https://httpbin.org/get")
print(response.status_code)   # 200
```

### 🏋️ Practice Exercises

1. Use `random` to generate a list of 5 random numbers between 1 and 50.
2. Use `datetime` to print today's date in `DD/MM/YYYY` format.
3. Use `os.path.exists()` to check if a file exists.
4. Create a module `math_utils.py` with `add`, `subtract`, `multiply`, `divide` functions.
5. Import and use your `math_utils.py` in another file.

### 🎯 Mini Challenge
Create a `string_utils.py` module with 5 utility functions (e.g., `is_email_valid`, `title_case`, `count_words`, `reverse_string`, `remove_spaces`). Import and test them.

### 📌 GitHub Commit
```
Day 11: Modules, imports, and creating reusable utilities
```

---

## Day 12 — List Comprehensions & Lambda Functions

### 📖 Concept (30 min)
List comprehensions are a Pythonic way to create lists in one line. Lambda functions are small anonymous functions. Both are used heavily in modern Python backends.

### 💻 Code Example

```python
# List comprehension
# Old way:
squares = []
for i in range(1, 6):
    squares.append(i ** 2)

# New way (list comprehension):
squares = [i ** 2 for i in range(1, 6)]
print(squares)   # [1, 4, 9, 16, 25]

# With condition
evens = [i for i in range(20) if i % 2 == 0]
print(evens)

# Transform a list
names = ["alice", "bob", "charlie"]
upper_names = [name.upper() for name in names]
print(upper_names)

# Filter a list
scores = [88, 45, 92, 61, 73, 38]
passing = [s for s in scores if s >= 60]
print(passing)   # [88, 92, 61, 73]

# Lambda functions (anonymous functions)
add = lambda a, b: a + b
print(add(3, 5))    # 8

square = lambda x: x ** 2
print(square(9))    # 81

# Lambda with sorted()
users = [
    {"name": "Charlie", "age": 30},
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 28}
]
sorted_users = sorted(users, key=lambda u: u["age"])
print(sorted_users)

# map() and filter() with lambda
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)   # [2, 4, 6, 8, 10]
```

### 🏋️ Practice Exercises

1. Use list comprehension to create a list of cubes from 1 to 10.
2. Filter a list of words to keep only those longer than 4 characters.
3. Convert a list of temperatures in Celsius to Fahrenheit using list comprehension.
4. Sort a list of dictionaries by a `"price"` key using lambda.
5. Use `map()` with lambda to square every number in a list.

### 🎯 Mini Challenge
Given a list of students with name and score, use list comprehension to create a new list of only passing students (score ≥ 60) sorted by score descending.

### 📌 GitHub Commit
```
Day 12: List comprehensions and lambda functions
```

---

## Day 13 — Basic Object-Oriented Programming (OOP)

### 📖 Concept (30 min)
OOP lets you model real-world things as objects. A **class** is a blueprint; an **object** is an instance of that blueprint.

Key concepts:
- `class` — defines the blueprint
- `__init__` — constructor, runs when object is created
- `self` — refers to the current object
- Methods — functions inside a class

### 💻 Code Example

```python
# Define a class
class User:
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.is_active = True

    def greet(self):
        return f"Hi, I'm {self.name}!"

    def deactivate(self):
        self.is_active = False
        return f"{self.name}'s account has been deactivated."

    def __str__(self):
        return f"User({self.name}, {self.email})"


# Create objects (instances)
user1 = User("Arjun", "arjun@example.com", 22)
user2 = User("Priya", "priya@example.com", 25)

print(user1.greet())          # Hi, I'm Arjun!
print(user2.email)            # priya@example.com
print(user1.deactivate())     # Arjun's account has been deactivated.
print(user1.is_active)        # False
print(str(user2))             # User(Priya, priya@example.com)


# A Product class
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def apply_discount(self, percent):
        self.price = self.price * (1 - percent / 100)
        return self.price

    def is_available(self):
        return self.stock > 0


laptop = Product("Laptop", 50000, 10)
print(laptop.apply_discount(10))   # 45000.0
print(laptop.is_available())       # True
```

### 🏋️ Practice Exercises

1. Create a `Car` class with `brand`, `model`, `speed`. Add a `accelerate(amount)` method.
2. Create a `BankAccount` class with `deposit()` and `withdraw()` methods.
3. Create a `Student` class with a `get_grade()` method based on marks.
4. Create a `Book` class and make a list of 3 book objects.
5. Add a `__str__` method to the `Car` class.

### 🎯 Mini Challenge
Build a `ShoppingCart` class that can `add_item(name, price)`, `remove_item(name)`, `get_total()`, and `show_items()`.

### 📌 GitHub Commit
```
Day 13: Object-oriented programming — classes and objects
```

---

## Day 14 — OOP Inheritance & Encapsulation

### 📖 Concept (30 min)
**Inheritance** lets a child class reuse the code of a parent class. **Encapsulation** hides internal details using private variables (prefix with `__`).

### 💻 Code Example

```python
# Inheritance
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        return f"{self.name} says {self.sound}!"


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "Woof")  # Call parent constructor

    def fetch(self):
        return f"{self.name} fetches the ball!"


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "Meow")

    def purr(self):
        return f"{self.name} is purring..."


dog = Dog("Bruno")
cat = Cat("Whiskers")
print(dog.speak())    # Bruno says Woof!
print(cat.speak())    # Whiskers says Meow!
print(dog.fetch())    # Bruno fetches the ball!


# Encapsulation with private attributes
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance    # Private! Can't access directly.

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited ₹{amount}. New balance: ₹{self.__balance}"

    def withdraw(self, amount):
        if amount > self.__balance:
            return "Insufficient funds!"
        self.__balance -= amount
        return f"Withdrew ₹{amount}. Remaining: ₹{self.__balance}"

    def get_balance(self):
        return self.__balance    # Controlled access via method


acc = BankAccount("Arjun", 10000)
print(acc.deposit(5000))     # Deposited ₹5000. New balance: ₹15000
print(acc.withdraw(3000))    # Withdrew ₹3000. Remaining: ₹12000
print(acc.get_balance())     # 12000
# print(acc.__balance)       # Error! Private attribute.
```

### 🏋️ Practice Exercises

1. Create a `Vehicle` parent class. Make `Car` and `Bike` inherit from it.
2. Override a method in the child class.
3. Use `super()` to call the parent's `__init__`.
4. Create a class with a private attribute `__pin` for a security PIN.
5. Write a `change_pin(old, new)` method that verifies the old PIN before changing.

### 🎯 Mini Challenge
Model a simple company system: `Employee` base class with `name`, `salary`. `Manager` subclass that adds a `team_size`. Both have a `get_info()` method but show different outputs.

### 📌 GitHub Commit
```
Day 14: OOP inheritance, encapsulation, and method overriding
```

---

## Day 15 — Working with APIs — Consuming APIs with `requests`

### 📖 Concept (30 min)
Before building APIs, learn how to **call** them. The `requests` library lets you make HTTP calls. You'll use this skill to test APIs and integrate third-party services.

Install: `pip install requests`

### 💻 Code Example

```python
import requests
import json

# GET request — fetch data
response = requests.get("https://jsonplaceholder.typicode.com/users/1")

print(response.status_code)   # 200
print(response.json())        # Dict with user data

user = response.json()
print(user["name"])
print(user["email"])

# GET a list
response = requests.get("https://jsonplaceholder.typicode.com/posts")
posts = response.json()
print(f"Total posts: {len(posts)}")
print(posts[0]["title"])

# POST request — send data
new_post = {
    "title": "My First Post",
    "body": "This is the content of my post.",
    "userId": 1
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=new_post
)
print(response.status_code)   # 201
print(response.json())

# Handle errors
def get_user(user_id):
    try:
        response = requests.get(
            f"https://jsonplaceholder.typicode.com/users/{user_id}",
            timeout=5
        )
        response.raise_for_status()   # Raises error if 4xx/5xx
        return response.json()
    except requests.exceptions.HTTPError as e:
        return f"HTTP Error: {e}"
    except requests.exceptions.Timeout:
        return "Request timed out"
    except requests.exceptions.ConnectionError:
        return "No internet connection"

print(get_user(1))
print(get_user(999))
```

### 🏋️ Practice Exercises

1. Fetch a random user from `https://randomuser.me/api/` and print their name.
2. Fetch 5 posts from JSONPlaceholder and print their titles.
3. Make a POST request to `https://httpbin.org/post` with your name and age.
4. Handle a timeout error with a 0.001 second timeout.
5. Check the response headers of any API request.

### 🎯 Mini Challenge
Build a weather fetcher using the Open-Meteo free API that accepts a latitude/longitude and prints current temperature.

### 📌 GitHub Commit
```
Day 15: Consuming REST APIs with the requests library
```

---

## Day 16 — Decorators

### 📖 Concept (30 min)
Decorators are functions that modify other functions. You'll see them **everywhere** in Flask: `@app.route("/")`, `@login_required`, etc.

Understanding decorators = understanding Flask.

### 💻 Code Example

```python
# A basic decorator
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before the function runs")
        result = func(*args, **kwargs)
        print("After the function runs")
        return result
    return wrapper


@my_decorator
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Arjun")
# Output:
# Before the function runs
# Hello, Arjun!
# After the function runs


# Practical decorator — timing a function
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper


@timer
def slow_function():
    time.sleep(1)
    return "Done!"

print(slow_function())


# Decorator that checks login (like in Flask)
def login_required(func):
    def wrapper(user, *args, **kwargs):
        if not user.get("logged_in"):
            return "Access denied. Please log in."
        return func(user, *args, **kwargs)
    return wrapper


@login_required
def view_dashboard(user):
    return f"Welcome to dashboard, {user['name']}!"

user1 = {"name": "Arjun", "logged_in": True}
user2 = {"name": "Guest", "logged_in": False}

print(view_dashboard(user1))   # Welcome to dashboard, Arjun!
print(view_dashboard(user2))   # Access denied. Please log in.
```

### 🏋️ Practice Exercises

1. Write a decorator that prints the function name before calling it.
2. Write a `retry(n)` decorator that retries a function `n` times on failure.
3. Write a `validate_positive` decorator that ensures all arguments are positive.
4. Write a `log_calls` decorator that counts how many times a function is called.
5. Stack two decorators on one function and observe the order of execution.

### 🎯 Mini Challenge
Build a `rate_limiter` decorator that allows a function to be called max 3 times. On the 4th call, return `"Rate limit exceeded."`.

### 📌 GitHub Commit
```
Day 16: Python decorators — theory and practical use cases
```

---

## Day 17 — Virtual Environments & pip

### 📖 Concept (30 min)
A virtual environment keeps your project's dependencies isolated from other projects. This is professional Python practice — always use one!

### 💻 Code Example

```bash
# Create a virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate

# On Mac/Linux:
source venv/bin/activate

# Install packages
pip install flask
pip install requests

# Save all dependencies to a file
pip freeze > requirements.txt

# Install from requirements.txt (for new developers cloning your repo)
pip install -r requirements.txt

# Deactivate
deactivate
```

```python
# requirements.txt example (auto-generated)
# Flask==3.0.0
# requests==2.31.0
# python-dotenv==1.0.0

# .env file — store secrets here (never commit to Git!)
# SECRET_KEY=mysupersecret
# DATABASE_URL=sqlite:///app.db

# Load .env in Python using python-dotenv
from dotenv import load_dotenv
import os

load_dotenv()

secret = os.getenv("SECRET_KEY")
print(secret)
```

### 🏋️ Practice Exercises

1. Create a virtual environment for a new project.
2. Install `flask` and `requests` in it.
3. Run `pip freeze > requirements.txt` and view the file.
4. Create a `.env` file with a fake `API_KEY` variable.
5. Read the `.env` variable in Python using `python-dotenv`.

### 🎯 Mini Challenge
Set up a clean project folder structure:
```
my_project/
├── venv/
├── .env
├── .gitignore
├── requirements.txt
└── app.py
```

### 📌 GitHub Commit
```
Day 17: Virtual environments, pip, and environment variables
```

---

## Day 18 — Git & GitHub Fundamentals

### 📖 Concept (30 min)
Git is the version control system every developer must know. GitHub is where you host your code online.

### 💻 Code Example

```bash
# Set up Git (first time only)
git config --global user.name "Your Name"
git config --global user.email "your@email.com"

# Initialize a repository
git init

# Check status
git status

# Stage changes
git add .          # Stage all files
git add app.py     # Stage one file

# Commit
git commit -m "Day 18: Initial project setup"

# Connect to GitHub
git remote add origin https://github.com/yourusername/repo-name.git
git branch -M main
git push -u origin main

# Everyday workflow
git status
git add .
git commit -m "Add user login endpoint"
git push

# View history
git log --oneline

# Create a branch
git checkout -b feature/user-auth

# Merge branch
git checkout main
git merge feature/user-auth
```

**`.gitignore` file:**
```
venv/
__pycache__/
*.pyc
.env
*.db
.DS_Store
```

### 🏋️ Practice Exercises

1. Initialize a Git repo in your project folder.
2. Create a `.gitignore` file with `venv/` and `.env`.
3. Make 3 commits with different changes.
4. Push the repo to GitHub.
5. Create a new branch called `feature/day18` and push it.

### 🎯 Mini Challenge
Set up your `90-days-python` GitHub repository with a proper `README.md`, `.gitignore`, and organized folders like `phase1/`, `phase2/`, etc.

### 📌 GitHub Commit
```
Day 18: Git workflow setup and GitHub repository created
```

---

## Day 19 — Python Review + Mini Project

### 📖 Concept (30 min)
Review all Phase 1 concepts. Today you'll build a small project combining everything you've learned.

**Phase 1 Checklist:**
- ✅ Variables & Data Types
- ✅ Strings & Lists & Dicts
- ✅ Conditions & Loops
- ✅ Functions
- ✅ Error Handling
- ✅ File I/O & JSON
- ✅ Modules
- ✅ OOP Basics
- ✅ Decorators
- ✅ Git & Virtual Environments

### 💻 Mini Project: Contact Book CLI App

```python
import json
import os

CONTACTS_FILE = "contacts.json"


def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as f:
            return json.load(f)
    return {}


def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as f:
        json.dump(contacts, f, indent=4)


def add_contact(name, phone, email):
    contacts = load_contacts()
    contacts[name] = {"phone": phone, "email": email}
    save_contacts(contacts)
    print(f"✅ Contact '{name}' added!")


def view_contacts():
    contacts = load_contacts()
    if not contacts:
        print("No contacts found.")
        return
    for name, info in contacts.items():
        print(f"\n📞 {name}")
        print(f"   Phone: {info['phone']}")
        print(f"   Email: {info['email']}")


def delete_contact(name):
    contacts = load_contacts()
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"🗑️ Contact '{name}' deleted!")
    else:
        print(f"Contact '{name}' not found.")


def search_contact(name):
    contacts = load_contacts()
    if name in contacts:
        info = contacts[name]
        print(f"Found: {name} — {info['phone']} — {info['email']}")
    else:
        print("Contact not found.")


if __name__ == "__main__":
    add_contact("Alice", "9876543210", "alice@example.com")
    add_contact("Bob", "8765432109", "bob@example.com")
    view_contacts()
    search_contact("Alice")
    delete_contact("Bob")
    view_contacts()
```

### 🎯 Mini Challenge
Add an `update_contact(name, phone=None, email=None)` function that updates only the provided fields.

### 📌 GitHub Commit
```
Day 19: Contact book CLI app — Phase 1 mini project
```

---

## Day 20 — Phase 1 Milestone 🏆

### 📖 Concept (30 min)
Consolidate your learnings, clean up your code, and push your full Phase 1 work to GitHub.

### 🎯 Phase 1 Final Challenge
Build a **Student Grade Manager** CLI:

```python
# Features to implement:
# 1. Add student (name + marks for 3 subjects)
# 2. Calculate average and grade (A/B/C/F)
# 3. List all students sorted by average
# 4. Save/load from JSON file
# 5. Find top scorer
# 6. Find students below passing (average < 60)

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks  # dict: {"math": 85, "english": 72, "science": 90}

    def average(self):
        return sum(self.marks.values()) / len(self.marks)

    def grade(self):
        avg = self.average()
        if avg >= 90: return "A"
        elif avg >= 75: return "B"
        elif avg >= 60: return "C"
        else: return "F"

    def to_dict(self):
        return {"name": self.name, "marks": self.marks}

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["marks"])
```

### 📌 GitHub Commit
```
Day 20: Phase 1 complete — Student grade manager final project
```

---

# Phase 2 — Backend Fundamentals with Flask (Day 21–45)

> Build real APIs. Learn how the web works.

---

## Day 21 — How the Web Works: HTTP Basics

### 📖 Concept (30 min)
Before Flask, understand what HTTP is. Every API call is an HTTP request.

**HTTP Methods:**
| Method | Action |
|--------|--------|
| GET | Retrieve data |
| POST | Create new data |
| PUT | Replace data |
| PATCH | Partially update data |
| DELETE | Remove data |

**HTTP Status Codes:**
| Code | Meaning |
|------|---------|
| 200 | OK |
| 201 | Created |
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
| 500 | Server Error |

### 💻 Code Example

```python
import requests

# Understanding requests and responses
response = requests.get("https://httpbin.org/get")

print("Status Code:", response.status_code)
print("Headers:", dict(response.headers))
print("Content-Type:", response.headers["Content-Type"])
print("Body:", response.json())

# POST with headers
headers = {"Content-Type": "application/json", "Authorization": "Bearer mytoken"}
data = {"username": "arjun", "password": "secret"}

response = requests.post(
    "https://httpbin.org/post",
    json=data,
    headers=headers
)
print(response.json())

# Different status codes
for code in [200, 201, 400, 401, 404, 500]:
    r = requests.get(f"https://httpbin.org/status/{code}")
    print(f"Status {code}: {r.status_code}")
```

### 🏋️ Practice Exercises

1. Make GET, POST, PUT, DELETE requests to `httpbin.org`.
2. Print the status code and response body of each.
3. Add custom headers to a request.
4. Send query parameters: `https://httpbin.org/get?name=Arjun&age=22`.
5. Parse the JSON body from a response.

### 🎯 Mini Challenge
Make a function `http_request(method, url, data=None)` that handles GET, POST, PUT, DELETE and always returns the status code and JSON body.

### 📌 GitHub Commit
```
Day 21: HTTP methods, status codes, and request-response cycle
```

---

## Day 22 — Flask Setup & First Route

### 📖 Concept (30 min)
Flask is a lightweight Python web framework. It lets you create web routes that respond to HTTP requests.

Install: `pip install flask`

A **route** is a URL pattern that your server handles. When someone visits `/users`, your Flask code decides what to return.

### 💻 Code Example

```python
# app.py
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to my API!",
        "status": "running"
    })


@app.route("/hello")
def hello():
    return jsonify({"message": "Hello, World!"})


@app.route("/about")
def about():
    return jsonify({
        "api": "My First Flask API",
        "version": "1.0",
        "author": "Arjun Singh"
    })


if __name__ == "__main__":
    app.run(debug=True)
```

```bash
# Run your Flask app
python app.py

# Visit: http://127.0.0.1:5000/
# Visit: http://127.0.0.1:5000/hello
# Visit: http://127.0.0.1:5000/about
```

### 🏋️ Practice Exercises

1. Create a Flask app with 3 routes: `/`, `/hello`, `/bye`.
2. Return a JSON response with your name and age from `/profile`.
3. Create a `/health` route that returns `{"status": "ok"}`.
4. Return a list of 5 items from `/items`.
5. Return a nested JSON object from `/user`.

### 🎯 Mini Challenge
Build a "Mini Info API" with routes: `/`, `/about`, `/contact`, `/skills`, `/projects` — each returning relevant mock data about you.

### 📌 GitHub Commit
```
Day 22: Flask setup, first API, and JSON responses
```

---

## Day 23 — URL Parameters & Query Strings

### 📖 Concept (30 min)
Routes can have **dynamic parts** (URL parameters) and **optional filters** (query strings).

- URL Parameter: `/users/42` → `user_id = 42`
- Query String: `/users?age=25&city=Mumbai`

### 💻 Code Example

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# URL parameter
@app.route("/users/<int:user_id>")
def get_user(user_id):
    return jsonify({
        "id": user_id,
        "name": f"User {user_id}",
        "email": f"user{user_id}@example.com"
    })


# String URL parameter
@app.route("/categories/<string:category>")
def get_category(category):
    return jsonify({"category": category})


# Query string parameters
@app.route("/search")
def search():
    query = request.args.get("q", "")
    limit = request.args.get("limit", 10, type=int)
    page = request.args.get("page", 1, type=int)

    return jsonify({
        "query": query,
        "limit": limit,
        "page": page,
        "results": [f"Result for '{query}' #{i}" for i in range(1, limit + 1)]
    })


# Multiple URL parameters
@app.route("/posts/<int:post_id>/comments/<int:comment_id>")
def get_comment(post_id, comment_id):
    return jsonify({
        "post_id": post_id,
        "comment_id": comment_id
    })


if __name__ == "__main__":
    app.run(debug=True)

# Test URLs:
# http://localhost:5000/users/1
# http://localhost:5000/users/42
# http://localhost:5000/search?q=python&limit=5&page=2
# http://localhost:5000/posts/1/comments/3
```

### 🏋️ Practice Exercises

1. Create a `/products/<int:id>` route that returns product details.
2. Create a `/greet/<string:name>` route that says hello.
3. Create `/users?role=admin&active=true` route that filters by query params.
4. Create a `/calculate/<int:a>/<int:b>` route that returns their sum.
5. Return a 404 response if user_id > 100.

### 🎯 Mini Challenge
Build a mini "Student API" with `/students/<int:id>` and `/students?grade=A&city=Mumbai` — return mock data based on params.

### 📌 GitHub Commit
```
Day 23: URL parameters and query strings in Flask
```

---

## Day 24 — Handling POST Requests & JSON Body

### 📖 Concept (30 min)
GET requests fetch data. POST requests **send data** to create something. The data comes in the **request body** as JSON.

### 💻 Code Example

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory data store (temporary, until we add DB)
users = []
user_id_counter = 1


@app.route("/users", methods=["GET"])
def get_users():
    return jsonify({"users": users, "total": len(users)})


@app.route("/users", methods=["POST"])
def create_user():
    global user_id_counter

    data = request.get_json()

    # Validate required fields
    if not data:
        return jsonify({"error": "No data provided"}), 400

    if "name" not in data or "email" not in data:
        return jsonify({"error": "name and email are required"}), 400

    new_user = {
        "id": user_id_counter,
        "name": data["name"],
        "email": data["email"],
        "age": data.get("age", None)
    }

    users.append(new_user)
    user_id_counter += 1

    return jsonify({"message": "User created", "user": new_user}), 201


@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    global users
    user = next((u for u in users if u["id"] == user_id), None)

    if not user:
        return jsonify({"error": "User not found"}), 404

    users = [u for u in users if u["id"] != user_id]
    return jsonify({"message": f"User {user_id} deleted"}), 200


if __name__ == "__main__":
    app.run(debug=True)
```

```bash
# Test with curl:
curl -X POST http://localhost:5000/users \
  -H "Content-Type: application/json" \
  -d '{"name": "Arjun", "email": "arjun@example.com", "age": 22}'
```

### 🏋️ Practice Exercises

1. Add a PUT endpoint to update a user's name by ID.
2. Add a PATCH endpoint to update only the email.
3. Return 400 if email doesn't contain `@`.
4. Add a `/users/<id>` GET endpoint to fetch a single user.
5. Return a count of users in the GET all response.

### 🎯 Mini Challenge
Build a complete CRUD API (Create, Read, Update, Delete) for a "Notes" resource with in-memory storage.

### 📌 GitHub Commit
```
Day 24: POST requests, JSON body, and in-memory CRUD API
```

---

## Day 25 — Request Validation & Error Handling in Flask

### 📖 Concept (30 min)
Good APIs always validate input and return clear error messages. Never trust user input — always validate before processing.

### 💻 Code Example

```python
from flask import Flask, jsonify, request
from functools import wraps

app = Flask(__name__)


# Custom error handler
@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Resource not found", "code": 404}), 404


@app.errorhandler(405)
def method_not_allowed(e):
    return jsonify({"error": "Method not allowed", "code": 405}), 405


@app.errorhandler(500)
def internal_error(e):
    return jsonify({"error": "Internal server error", "code": 500}), 500


# Validation helper function
def validate_user_data(data):
    errors = []
    if not data.get("name"):
        errors.append("Name is required")
    elif len(data["name"]) < 2:
        errors.append("Name must be at least 2 characters")

    if not data.get("email"):
        errors.append("Email is required")
    elif "@" not in data["email"]:
        errors.append("Invalid email format")

    if "age" in data:
        if not isinstance(data["age"], int):
            errors.append("Age must be a number")
        elif data["age"] < 1 or data["age"] > 120:
            errors.append("Age must be between 1 and 120")

    return errors


@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body must be JSON"}), 400

    errors = validate_user_data(data)
    if errors:
        return jsonify({"error": "Validation failed", "details": errors}), 422

    # All good — process the data
    return jsonify({"message": "User created", "data": data}), 201


if __name__ == "__main__":
    app.run(debug=True)
```

### 🏋️ Practice Exercises

1. Add validation for a `phone` field (must be 10 digits).
2. Add a custom 400 error handler.
3. Validate that a password is at least 8 characters.
4. Return all validation errors at once (not just the first one).
5. Write a reusable `validate_required(data, fields)` function.

### 🎯 Mini Challenge
Build a registration endpoint `/register` that validates: name (min 2 chars), email (has `@`), password (min 8 chars, must have a number), age (18-100). Return all errors at once.

### 📌 GitHub Commit
```
Day 25: Input validation and custom error handling in Flask
```

---

## Day 26 — Flask Blueprints & Project Structure

### 📖 Concept (30 min)
As your app grows, one `app.py` file becomes messy. **Blueprints** let you split routes into separate files by feature. This is how real projects are structured.

### 💻 Code Example

```
project/
├── app.py
├── requirements.txt
├── routes/
│   ├── __init__.py
│   ├── users.py
│   └── products.py
└── models/
    └── __init__.py
```

```python
# routes/users.py
from flask import Blueprint, jsonify, request

users_bp = Blueprint("users", __name__, url_prefix="/users")

users_db = []

@users_bp.route("/", methods=["GET"])
def get_all_users():
    return jsonify({"users": users_db})

@users_bp.route("/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = next((u for u in users_db if u["id"] == user_id), None)
    if not user:
        return jsonify({"error": "Not found"}), 404
    return jsonify(user)

@users_bp.route("/", methods=["POST"])
def create_user():
    data = request.get_json()
    users_db.append(data)
    return jsonify(data), 201
```

```python
# routes/products.py
from flask import Blueprint, jsonify

products_bp = Blueprint("products", __name__, url_prefix="/products")

@products_bp.route("/")
def get_products():
    return jsonify({"products": []})
```

```python
# app.py
from flask import Flask
from routes.users import users_bp
from routes.products import products_bp

app = Flask(__name__)
app.register_blueprint(users_bp)
app.register_blueprint(products_bp)

@app.route("/")
def home():
    return {"message": "API is running"}

if __name__ == "__main__":
    app.run(debug=True)
```

### 🏋️ Practice Exercises

1. Create a `routes/` folder and move user routes to `users.py`.
2. Create a `products.py` blueprint with GET and POST.
3. Register both blueprints in `app.py`.
4. Add a `routes/auth.py` blueprint with a `/login` placeholder.
5. Test all routes via Postman or browser.

### 🎯 Mini Challenge
Restructure your Day 24 CRUD Notes API into a properly structured project with Blueprints.

### 📌 GitHub Commit
```
Day 26: Flask blueprints and professional project structure
```

---

## Day 27–28 — Building a Complete REST API

### 📖 Concept (30 min each day)
Build a fully functional Books API combining all Phase 2 concepts so far.

### 💻 Code Example

```python
# Full Books REST API
from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
    {"id": 1, "title": "Clean Code", "author": "Robert Martin", "price": 499, "genre": "Programming"},
    {"id": 2, "title": "The Pragmatic Programmer", "author": "David Thomas", "price": 599, "genre": "Programming"},
]
next_id = 3


@app.route("/api/books", methods=["GET"])
def get_books():
    genre = request.args.get("genre")
    filtered = [b for b in books if b["genre"] == genre] if genre else books
    return jsonify({"books": filtered, "count": len(filtered)})


@app.route("/api/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book = next((b for b in books if b["id"] == book_id), None)
    return jsonify(book) if book else (jsonify({"error": "Not found"}), 404)


@app.route("/api/books", methods=["POST"])
def create_book():
    global next_id
    data = request.get_json()
    if not data or not all(k in data for k in ["title", "author", "price"]):
        return jsonify({"error": "title, author, price required"}), 400
    data["id"] = next_id
    next_id += 1
    books.append(data)
    return jsonify(data), 201


@app.route("/api/books/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    book = next((b for b in books if b["id"] == book_id), None)
    if not book:
        return jsonify({"error": "Not found"}), 404
    data = request.get_json()
    book.update(data)
    return jsonify(book)


@app.route("/api/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    global books
    book = next((b for b in books if b["id"] == book_id), None)
    if not book:
        return jsonify({"error": "Not found"}), 404
    books = [b for b in books if b["id"] != book_id]
    return jsonify({"message": "Book deleted"})


if __name__ == "__main__":
    app.run(debug=True)
```

### 📌 GitHub Commit (Day 27)
```
Day 27: Books REST API — GET, POST endpoints
```

### 📌 GitHub Commit (Day 28)
```
Day 28: Books REST API — PUT, DELETE, and query filters complete
```

---

## Day 29 — API Testing with Postman

### 📖 Concept (30 min)
Postman is a GUI tool for testing APIs. Every backend developer uses it. Learn to test all your endpoints properly.

### 💻 Postman Test Collection Setup

```
Collection: My Flask API Tests
├── GET all books         — GET http://localhost:5000/api/books
├── GET one book          — GET http://localhost:5000/api/books/1
├── GET books by genre    — GET http://localhost:5000/api/books?genre=Programming
├── POST create book      — POST http://localhost:5000/api/books
├── PUT update book       — PUT http://localhost:5000/api/books/1
└── DELETE book           — DELETE http://localhost:5000/api/books/1
```

```json
// POST Body (raw JSON):
{
    "title": "Python Crash Course",
    "author": "Eric Matthes",
    "price": 450,
    "genre": "Programming"
}
```

```python
# You can also test with Python
import requests

BASE = "http://localhost:5000/api"

# Test GET
r = requests.get(f"{BASE}/books")
assert r.status_code == 200
print("GET all books ✅")

# Test POST
new_book = {"title": "Test Book", "author": "Tester", "price": 100}
r = requests.post(f"{BASE}/books", json=new_book)
assert r.status_code == 201
book_id = r.json()["id"]
print("POST create book ✅")

# Test GET single
r = requests.get(f"{BASE}/books/{book_id}")
assert r.status_code == 200
print("GET single book ✅")

# Test DELETE
r = requests.delete(f"{BASE}/books/{book_id}")
assert r.status_code == 200
print("DELETE book ✅")

print("All tests passed! 🎉")
```

### 📌 GitHub Commit
```
Day 29: API testing with Postman and automated test scripts
```

---

## Day 30 — Middleware & CORS

### 📖 Concept (30 min)
Middleware runs before/after every request. CORS (Cross-Origin Resource Sharing) allows your API to be called from a frontend on a different domain.

Install: `pip install flask-cors`

### 💻 Code Example

```python
from flask import Flask, jsonify, request, g
from flask_cors import CORS
import time
import uuid

app = Flask(__name__)
CORS(app)  # Allow all origins

# Or more controlled:
# CORS(app, resources={r"/api/*": {"origins": ["https://myapp.com"]}})


# Middleware: Before every request
@app.before_request
def before_request():
    g.start_time = time.time()
    g.request_id = str(uuid.uuid4())[:8]
    print(f"[{g.request_id}] {request.method} {request.path}")


# Middleware: After every request
@app.after_request
def after_request(response):
    duration = time.time() - g.start_time
    response.headers["X-Request-ID"] = g.request_id
    response.headers["X-Response-Time"] = f"{duration:.3f}s"
    print(f"[{g.request_id}] Response: {response.status_code} in {duration:.3f}s")
    return response


@app.route("/api/data")
def get_data():
    return jsonify({"message": "Here is your data!", "request_id": g.request_id})


if __name__ == "__main__":
    app.run(debug=True)
```

### 📌 GitHub Commit
```
Day 30: Middleware, CORS, and request lifecycle in Flask
```

---

## Day 31–35 — Flask Deep Dive (Authentication Concepts, JWT, File Uploads)

> Over 5 days, build deeper Flask skills.

### Day 31 — Flask Configuration & Environment Management

```python
# config.py
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig
}

# app.py
from flask import Flask
from config import config
import os

app = Flask(__name__)
env = os.getenv("FLASK_ENV", "default")
app.config.from_object(config[env])
```

**Commit:** `Day 31: Flask configuration with environment management`

---

### Day 32 — Hashing Passwords

```python
# pip install bcrypt
import bcrypt

def hash_password(plain_password: str) -> str:
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(plain_password.encode("utf-8"), salt)
    return hashed.decode("utf-8")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(
        plain_password.encode("utf-8"),
        hashed_password.encode("utf-8")
    )

# Usage
password = "MySuperSecret123"
hashed = hash_password(password)
print(f"Hashed: {hashed}")
print(f"Valid: {verify_password(password, hashed)}")       # True
print(f"Invalid: {verify_password('wrongpass', hashed)}")  # False
```

**Commit:** `Day 32: Password hashing with bcrypt`

---

### Day 33 — JWT Tokens

```python
# pip install PyJWT
import jwt
import datetime

SECRET_KEY = "my-secret-key"

def generate_token(user_id: int) -> str:
    payload = {
        "user_id": user_id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=24),
        "iat": datetime.datetime.utcnow()
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

def decode_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return {"valid": True, "user_id": payload["user_id"]}
    except jwt.ExpiredSignatureError:
        return {"valid": False, "error": "Token expired"}
    except jwt.InvalidTokenError:
        return {"valid": False, "error": "Invalid token"}

token = generate_token(42)
print(f"Token: {token}")
print(f"Decoded: {decode_token(token)}")
```

**Commit:** `Day 33: JWT token generation and verification`

---

### Day 34 — Auth Decorator (Protecting Routes)

```python
from flask import Flask, jsonify, request
import jwt

app = Flask(__name__)
SECRET_KEY = "my-secret-key"

def token_required(f):
    from functools import wraps
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get("Authorization", "").replace("Bearer ", "")
        if not token:
            return jsonify({"error": "Token missing"}), 401
        try:
            data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            request.user_id = data["user_id"]
        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token expired"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"error": "Invalid token"}), 401
        return f(*args, **kwargs)
    return decorated

@app.route("/protected")
@token_required
def protected():
    return jsonify({"message": f"Hello User {request.user_id}!"})
```

**Commit:** `Day 34: JWT auth decorator for protecting Flask routes`

---

### Day 35 — File Uploads in Flask

```python
import os
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads"
app.config["MAX_CONTENT_LENGTH"] = 2 * 1024 * 1024  # 2MB limit
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "pdf"}

os.makedirs("uploads", exist_ok=True)

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400
    file = request.files["file"]
    if not allowed_file(file.filename):
        return jsonify({"error": "File type not allowed"}), 400
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
    return jsonify({"message": "File uploaded", "filename": filename}), 201
```

**Commit:** `Day 35: File uploads in Flask with validation`

---

## Day 36–40 — REST API Best Practices & Rate Limiting

### Day 36 — Pagination

```python
@app.route("/api/posts")
def get_posts():
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 10, type=int)
    per_page = min(per_page, 100)   # Cap at 100

    # Simulate 50 posts
    all_posts = [{"id": i, "title": f"Post {i}"} for i in range(1, 51)]

    start = (page - 1) * per_page
    end = start + per_page
    paginated = all_posts[start:end]

    return jsonify({
        "data": paginated,
        "pagination": {
            "page": page,
            "per_page": per_page,
            "total": len(all_posts),
            "pages": (len(all_posts) + per_page - 1) // per_page
        }
    })
```

**Commit:** `Day 36: API pagination implementation`

---

### Day 37–40 — Rapid API Build Days

Over these 4 days, focus on building and iterating:

- **Day 37:** Build a `/api/todos` CRUD API with in-memory storage
- **Day 38:** Add pagination + filtering to todos
- **Day 39:** Add JWT auth to protect todo routes
- **Day 40:** Add validation, error handling, and write test scripts

**Commits:**
```
Day 37: Todo API — CRUD endpoints
Day 38: Todo API — pagination and filtering
Day 39: Todo API — JWT authentication added
Day 40: Todo API — complete with tests and validation
```

---

## Day 41–45 — Phase 2 Review & Milestone Project

### Day 41–44 — Build a Products Catalog API

Build a complete, production-style Products API:

```
Endpoints:
GET    /api/products              — List (with search, filter, pagination)
GET    /api/products/<id>         — Get single product
POST   /api/products              — Create (auth required)
PUT    /api/products/<id>         — Update (auth required)
DELETE /api/products/<id>         — Delete (auth required)
POST   /api/auth/register         — Register user
POST   /api/auth/login            — Login, returns JWT token
```

**Commit:** `Day 44: Products Catalog API — Phase 2 milestone project complete`

---

### Day 45 — Phase 2 Milestone 🏆

Review all Phase 2 skills:
- ✅ HTTP Methods & Status Codes
- ✅ Flask Routing & Blueprints
- ✅ JSON Request/Response
- ✅ Input Validation
- ✅ Error Handling
- ✅ JWT Authentication
- ✅ Pagination & Filtering
- ✅ Postman Testing

**Commit:** `Day 45: Phase 2 complete — REST API fundamentals mastered`

---

# Phase 3 — Databases (Day 46–65)

> Make your data persist. No more losing data on restart!

---

## Day 46 — SQL Basics: What is a Database?

### 📖 Concept (30 min)
A database stores data permanently. SQL (Structured Query Language) is used to talk to relational databases.

**Key concepts:**
- **Table** — like a spreadsheet with rows and columns
- **Row** — one record (one user, one product)
- **Column** — one field (name, email, age)
- **Primary Key** — unique ID for each row
- **Foreign Key** — a reference to another table's ID

### 💻 Code Example

```sql
-- Create a table
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    age INTEGER,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Insert data
INSERT INTO users (name, email, age) VALUES ('Arjun', 'arjun@example.com', 22);
INSERT INTO users (name, email, age) VALUES ('Priya', 'priya@example.com', 25);

-- Read data
SELECT * FROM users;
SELECT name, email FROM users;
SELECT * FROM users WHERE age > 20;
SELECT * FROM users ORDER BY name ASC;
SELECT * FROM users LIMIT 10;

-- Update
UPDATE users SET age = 23 WHERE name = 'Arjun';

-- Delete
DELETE FROM users WHERE id = 1;
```

```python
# Working with SQLite in Python
import sqlite3

conn = sqlite3.connect("test.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL
    )
""")
conn.commit()
conn.close()
print("Database and table created!")
```

### 📌 GitHub Commit
```
Day 46: SQL basics — tables, queries, and SQLite setup
```

---

## Day 47 — CRUD Operations with SQLite

### 💻 Code Example

```python
import sqlite3

DATABASE = "app.db"

def get_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Rows as dicts!
    return conn

def init_db():
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                age INTEGER
            )
        """)

# CREATE
def create_user(name, email, age):
    with get_connection() as conn:
        cursor = conn.execute(
            "INSERT INTO users (name, email, age) VALUES (?, ?, ?)",
            (name, email, age)
        )
        return cursor.lastrowid

# READ
def get_all_users():
    with get_connection() as conn:
        rows = conn.execute("SELECT * FROM users").fetchall()
        return [dict(row) for row in rows]

def get_user_by_id(user_id):
    with get_connection() as conn:
        row = conn.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()
        return dict(row) if row else None

# UPDATE
def update_user(user_id, name=None, age=None):
    with get_connection() as conn:
        if name:
            conn.execute("UPDATE users SET name = ? WHERE id = ?", (name, user_id))
        if age:
            conn.execute("UPDATE users SET age = ? WHERE id = ?", (age, user_id))

# DELETE
def delete_user(user_id):
    with get_connection() as conn:
        conn.execute("DELETE FROM users WHERE id = ?", (user_id,))

# Test it all
init_db()
id1 = create_user("Arjun", "arjun@example.com", 22)
id2 = create_user("Priya", "priya@example.com", 25)
print(get_all_users())
print(get_user_by_id(id1))
update_user(id1, name="Arjun Kumar")
delete_user(id2)
print(get_all_users())
```

### 📌 GitHub Commit
```
Day 47: SQLite CRUD operations — Create, Read, Update, Delete
```

---

## Day 48–50 — Connecting Flask with SQLite

### 💻 Full Flask + SQLite Integration

```python
# database.py
import sqlite3
from flask import g

DATABASE = "app.db"

def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db(e=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()

def init_db(app):
    with app.app_context():
        db = get_db()
        db.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price REAL NOT NULL,
                stock INTEGER DEFAULT 0,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        db.commit()
    app.teardown_appcontext(close_db)
```

```python
# routes/products.py
from flask import Blueprint, jsonify, request, g
from database import get_db

products_bp = Blueprint("products", __name__, url_prefix="/api/products")

@products_bp.route("/", methods=["GET"])
def get_products():
    db = get_db()
    rows = db.execute("SELECT * FROM products").fetchall()
    return jsonify({"products": [dict(r) for r in rows]})

@products_bp.route("/", methods=["POST"])
def create_product():
    data = request.get_json()
    if not data or not all(k in data for k in ["name", "price"]):
        return jsonify({"error": "name and price required"}), 400
    db = get_db()
    cursor = db.execute(
        "INSERT INTO products (name, price, stock) VALUES (?, ?, ?)",
        (data["name"], data["price"], data.get("stock", 0))
    )
    db.commit()
    return jsonify({"id": cursor.lastrowid, **data}), 201
```

**Commits:**
```
Day 48: Flask + SQLite connection setup
Day 49: Products CRUD API with SQLite database
Day 50: Database query optimization and search
```

---

## Day 51–55 — SQLAlchemy ORM

### 📖 Concept
SQLAlchemy is an ORM (Object Relational Mapper). Instead of writing raw SQL, you work with Python classes.

Install: `pip install flask-sqlalchemy`

### 💻 Code Example

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


# Models — Python classes = Database tables
class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    age = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    posts = db.relationship("Post", backref="author", lazy=True)

    def to_dict(self):
        return {
            "id": self.id, "name": self.name,
            "email": self.email, "age": self.age
        }


class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


with app.app_context():
    db.create_all()


@app.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify({"users": [u.to_dict() for u in users]})


@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    user = User(name=data["name"], email=data["email"], age=data.get("age"))
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_dict()), 201


@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify(user.to_dict())


@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "Deleted"})
```

**Commits:**
```
Day 51: SQLAlchemy setup and User model
Day 52: SQLAlchemy relationships — User and Post models
Day 53: SQLAlchemy queries — filter, order, paginate
Day 54: Database migrations concept and schema changes
Day 55: Full Flask + SQLAlchemy CRUD API complete
```

---

## Day 56–60 — Advanced SQL Queries

### 💻 Code Examples

```sql
-- JOINS
SELECT users.name, posts.title
FROM posts
JOIN users ON posts.user_id = users.id;

-- Aggregate functions
SELECT COUNT(*) as total_users FROM users;
SELECT AVG(age) as avg_age FROM users;
SELECT MAX(price), MIN(price) FROM products;

-- GROUP BY
SELECT genre, COUNT(*) as count
FROM books
GROUP BY genre
ORDER BY count DESC;

-- HAVING (filter after GROUP BY)
SELECT user_id, COUNT(*) as post_count
FROM posts
GROUP BY user_id
HAVING post_count > 5;

-- Subquery
SELECT name FROM users
WHERE id IN (
    SELECT user_id FROM orders WHERE total > 1000
);
```

```python
# SQLAlchemy equivalents
from sqlalchemy import func

# Count
count = db.session.query(func.count(User.id)).scalar()

# Average
avg_age = db.session.query(func.avg(User.age)).scalar()

# Join
results = db.session.query(User, Post).join(Post).all()

# Filter
active_users = User.query.filter_by(is_active=True).all()
young_users = User.query.filter(User.age < 30).all()

# Order and limit
top_5 = User.query.order_by(User.created_at.desc()).limit(5).all()
```

**Commits:**
```
Day 56: SQL JOINs — combining tables
Day 57: Aggregate functions — COUNT, AVG, SUM, MAX, MIN
Day 58: GROUP BY, HAVING, and subqueries
Day 59: SQLAlchemy advanced queries
Day 60: Database indexing and query performance
```

---

## Day 61–65 — Phase 3 Milestone: Full Database-Backed API

Build a **Blog API** with Users, Posts, Tags, and Comments:

```
Tables:
- users (id, name, email, password_hash)
- posts (id, title, content, user_id, created_at)
- comments (id, content, post_id, user_id, created_at)
- tags (id, name)
- post_tags (post_id, tag_id)  — many-to-many
```

**Commits:**
```
Day 61: Blog API — models and database schema
Day 62: Blog API — user and auth endpoints
Day 63: Blog API — posts CRUD endpoints
Day 64: Blog API — comments and tags
Day 65: Phase 3 complete — Blog API with full database integration
```

---

# Phase 4 — Real Backend Projects (Day 66–90)

> Portfolio-worthy, job-ready projects.

---

## Project 1: Authentication API (Day 66–73)

### 📖 Overview
A complete authentication system with registration, login, JWT tokens, password reset, and protected routes.

### 📁 Project Structure

```
auth_api/
├── app.py
├── config.py
├── models/
│   └── user.py
├── routes/
│   └── auth.py
├── utils/
│   ├── jwt_helper.py
│   └── email_helper.py
├── requirements.txt
└── README.md
```

### 💻 Key Code

```python
# models/user.py
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import bcrypt

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    is_verified = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        self.password_hash = bcrypt.hashpw(
            password.encode(), bcrypt.gensalt()
        ).decode()

    def check_password(self, password):
        return bcrypt.checkpw(
            password.encode(), self.password_hash.encode()
        )

    def to_dict(self):
        return {"id": self.id, "name": self.name, "email": self.email}
```

```python
# routes/auth.py
from flask import Blueprint, jsonify, request
from models.user import User, db
from utils.jwt_helper import generate_token, token_required

auth_bp = Blueprint("auth", __name__, url_prefix="/api/auth")


@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    if User.query.filter_by(email=data.get("email")).first():
        return jsonify({"error": "Email already registered"}), 409

    user = User(name=data["name"], email=data["email"])
    user.set_password(data["password"])
    db.session.add(user)
    db.session.commit()

    token = generate_token(user.id)
    return jsonify({
        "message": "Registered successfully",
        "token": token,
        "user": user.to_dict()
    }), 201


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data.get("email")).first()

    if not user or not user.check_password(data.get("password", "")):
        return jsonify({"error": "Invalid credentials"}), 401

    token = generate_token(user.id)
    return jsonify({
        "message": "Login successful",
        "token": token,
        "user": user.to_dict()
    })


@auth_bp.route("/me", methods=["GET"])
@token_required
def get_profile(current_user):
    return jsonify(current_user.to_dict())


@auth_bp.route("/change-password", methods=["POST"])
@token_required
def change_password(current_user):
    data = request.get_json()
    if not current_user.check_password(data.get("old_password", "")):
        return jsonify({"error": "Wrong current password"}), 400
    current_user.set_password(data["new_password"])
    db.session.commit()
    return jsonify({"message": "Password changed successfully"})
```

### API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/auth/register` | Register new user |
| POST | `/api/auth/login` | Login, get JWT token |
| GET | `/api/auth/me` | Get profile (auth required) |
| POST | `/api/auth/change-password` | Change password (auth required) |
| POST | `/api/auth/logout` | Logout (invalidate token) |

**Commits:**
```
Day 66: Auth API — project setup and User model
Day 67: Auth API — register endpoint with validation
Day 68: Auth API — login and JWT token generation
Day 69: Auth API — protected routes and token middleware
Day 70: Auth API — password change endpoint
Day 71: Auth API — refresh token mechanism
Day 72: Auth API — complete testing with Postman
Day 73: Auth API v1.0 — final polish and README
```

---

## Project 2: Task Manager API (Day 74–79)

### 📖 Overview
A full-featured task management API with user authentication, task CRUD, priority levels, deadlines, and filtering.

### 💻 Key Models

```python
# models/task.py
from datetime import datetime
from models.user import db

class Task(db.Model):
    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    status = db.Column(db.String(20), default="pending")  # pending/in_progress/done
    priority = db.Column(db.String(10), default="medium")  # low/medium/high
    due_date = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status,
            "priority": self.priority,
            "due_date": self.due_date.isoformat() if self.due_date else None,
            "created_at": self.created_at.isoformat()
        }
```

### API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/tasks` | List all tasks (auth required) |
| POST | `/api/tasks` | Create task |
| GET | `/api/tasks/<id>` | Get single task |
| PUT | `/api/tasks/<id>` | Update task |
| PATCH | `/api/tasks/<id>/status` | Update status only |
| DELETE | `/api/tasks/<id>` | Delete task |
| GET | `/api/tasks?status=done&priority=high` | Filter tasks |
| GET | `/api/tasks/stats` | Task statistics |

**Commits:**
```
Day 74: Task Manager API — setup and Task model
Day 75: Task Manager API — CRUD endpoints
Day 76: Task Manager API — filtering, sorting, pagination
Day 77: Task Manager API — task statistics endpoint
Day 78: Task Manager API — testing and bug fixes
Day 79: Task Manager API v1.0 — complete with docs
```

---

## Project 3: Tournament Management API (Day 80–85)

### 📖 Overview
A sports tournament management system with teams, players, fixtures, results, and standings.

### 💻 Key Models

```python
# Tournament, Team, Player, Match, Standing models

class Tournament(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    sport = db.Column(db.String(50), nullable=False)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    status = db.Column(db.String(20), default="upcoming")
    teams = db.relationship("Team", backref="tournament", lazy=True)

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    tournament_id = db.Column(db.Integer, db.ForeignKey("tournament.id"))
    players = db.relationship("Player", backref="team", lazy=True)

class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tournament_id = db.Column(db.Integer, db.ForeignKey("tournament.id"))
    home_team_id = db.Column(db.Integer, db.ForeignKey("team.id"))
    away_team_id = db.Column(db.Integer, db.ForeignKey("team.id"))
    home_score = db.Column(db.Integer, default=0)
    away_score = db.Column(db.Integer, default=0)
    status = db.Column(db.String(20), default="scheduled")
    match_date = db.Column(db.DateTime)
```

### API Endpoints

```
POST /api/tournaments                   — Create tournament
GET  /api/tournaments/<id>/teams        — List teams
POST /api/tournaments/<id>/teams        — Register team
POST /api/tournaments/<id>/fixtures     — Generate fixtures
POST /api/matches/<id>/result           — Enter match result
GET  /api/tournaments/<id>/standings    — View standings/leaderboard
```

**Commits:**
```
Day 80: Tournament API — project setup and models
Day 81: Tournament API — tournament and team endpoints
Day 82: Tournament API — fixture generation algorithm
Day 83: Tournament API — match result and standings calculation
Day 84: Tournament API — leaderboard and statistics
Day 85: Tournament API v1.0 — final polish and documentation
```

---

## Project 4: Chat API with Message Storage (Day 86–90)

### 📖 Overview
A real-time chat API with rooms, message history, users, and read receipts — the most complex project.

### 💻 Key Models & Endpoints

```python
class ChatRoom(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    room_type = db.Column(db.String(20), default="group")  # "direct" or "group"
    created_by = db.Column(db.Integer, db.ForeignKey("users.id"))
    messages = db.relationship("Message", backref="room", lazy=True)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    room_id = db.Column(db.Integer, db.ForeignKey("chat_room.id"))
    sender_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    message_type = db.Column(db.String(20), default="text")  # text/image/file
    is_deleted = db.Column(db.Boolean, default=False)
    sent_at = db.Column(db.DateTime, default=datetime.utcnow)

class RoomMember(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    room_id = db.Column(db.Integer, db.ForeignKey("chat_room.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    last_read_at = db.Column(db.DateTime)
    joined_at = db.Column(db.DateTime, default=datetime.utcnow)
```

```python
# Key endpoints
@chat_bp.route("/rooms", methods=["POST"])
@token_required
def create_room(current_user): ...

@chat_bp.route("/rooms/<int:room_id>/messages", methods=["GET"])
@token_required
def get_messages(current_user, room_id):
    page = request.args.get("page", 1, type=int)
    messages = Message.query.filter_by(room_id=room_id, is_deleted=False)\
        .order_by(Message.sent_at.desc())\
        .paginate(page=page, per_page=50)
    return jsonify({
        "messages": [m.to_dict() for m in messages.items],
        "has_more": messages.has_next
    })

@chat_bp.route("/rooms/<int:room_id>/messages", methods=["POST"])
@token_required
def send_message(current_user, room_id): ...

@chat_bp.route("/rooms/<int:room_id>/read", methods=["POST"])
@token_required
def mark_as_read(current_user, room_id): ...
```

**Commits:**
```
Day 86: Chat API — project setup and models
Day 87: Chat API — room management endpoints
Day 88: Chat API — message send and history endpoints
Day 89: Chat API — read receipts and unread count
Day 90: Chat API v1.0 — FINAL PROJECT COMPLETE 🎉
```

---

# Final GitHub Portfolio Structure

```
github.com/yourusername/
│
├── 90-days-python/                    ← Main learning repo
│   ├── README.md                      ← This file!
│   ├── phase1/                        ← Python fundamentals
│   │   ├── day01_hello_world.py
│   │   ├── day02_variables.py
│   │   ├── ...
│   │   ├── day19_contact_book/
│   │   └── day20_grade_manager/
│   ├── phase2/                        ← Flask APIs
│   │   ├── day22_first_flask/
│   │   ├── day27_books_api/
│   │   └── day41_products_api/
│   ├── phase3/                        ← Databases
│   │   ├── day46_sql_basics/
│   │   ├── day47_sqlite_crud/
│   │   └── day61_blog_api/
│   └── phase4/                        ← Projects
│       ├── auth_api/
│       ├── task_manager_api/
│       ├── tournament_api/
│       └── chat_api/
│
├── auth-api/                          ← Standalone project repo
│   ├── README.md
│   ├── app.py
│   ├── models/
│   ├── routes/
│   ├── requirements.txt
│   └── .gitignore
│
├── task-manager-api/                  ← Standalone project repo
│   └── ...
│
├── tournament-api/                    ← Standalone project repo
│   └── ...
│
└── chat-api/                          ← Standalone project repo
    └── ...
```

---

# ✅ Completed Projects

| # | Project | Tech | Endpoints | Description |
|---|---------|------|-----------|-------------|
| 1 | Contact Book CLI | Python, JSON | — | CRUD CLI app with file storage |
| 2 | Books REST API | Flask | 5 endpoints | Full CRUD with in-memory storage |
| 3 | Products Catalog API | Flask, JWT | 8 endpoints | Authenticated products API |
| 4 | Blog API | Flask, SQLAlchemy | 12 endpoints | Multi-table database API |
| 5 | **Authentication API** | Flask, SQLAlchemy, JWT, bcrypt | 8 endpoints | Complete auth system |
| 6 | **Task Manager API** | Flask, SQLAlchemy, JWT | 9 endpoints | Task CRUD with filters & stats |
| 7 | **Tournament API** | Flask, SQLAlchemy | 10 endpoints | Fixture generation & standings |
| 8 | **Chat API** | Flask, SQLAlchemy, JWT | 8 endpoints | Rooms, messages, read receipts |

---

# 🛠️ Skills Learned

### Python
- Variables, Data Types, Strings, Lists, Dicts
- Conditions, Loops, Functions
- Error Handling, File I/O, JSON
- OOP (Classes, Inheritance, Encapsulation)
- Decorators, Comprehensions, Lambda
- Modules, Virtual Environments, pip

### Web & APIs
- HTTP Protocol, Methods, Status Codes
- REST API Design Principles
- Request/Response Cycle
- JSON Data Format
- CORS, Middleware
- API Testing with Postman

### Flask
- Routing, Blueprints, URL Parameters
- Request Validation & Error Handling
- JWT Authentication
- File Uploads
- Pagination & Filtering
- Flask-SQLAlchemy ORM

### Databases
- SQL — CREATE, INSERT, SELECT, UPDATE, DELETE
- Joins, Aggregates, Subqueries
- SQLite & SQLAlchemy ORM
- Database Relationships (1:1, 1:N, N:M)
- Schema Design

### Tools & DevOps
- Git & GitHub
- Virtual Environments
- Environment Variables (.env)
- Postman API Testing
- Python Package Management

---

# 📚 Recommended Resources

| Resource | Link |
|----------|------|
| Python Official Docs | https://docs.python.org |
| Flask Official Docs | https://flask.palletsprojects.com |
| SQLAlchemy Docs | https://docs.sqlalchemy.org |
| JWT Guide | https://jwt.io |
| HTTP Status Codes | https://developer.mozilla.org/en-US/docs/Web/HTTP/Status |
| Git Cheatsheet | https://education.github.com/git-cheat-sheet-education.pdf |
| Postman Learning | https://learning.postman.com |

---

# 🎓 You're Job-Ready!

After completing this 90-day plan, you can apply for:

- **Junior Python Developer**
- **Junior Backend Developer**
- **Python Flask Developer**
- **API Developer**
- **Junior Full Stack Developer** (pair with a React course)

Your GitHub portfolio now has **4 real projects** demonstrating:
- Clean code & project structure
- REST API design
- Authentication & security
- Database integration
- Git workflow

---

> 💡 **Pro Tip:** Keep building. Pick one more project idea and build it independently. The best way to learn is to build things you actually want to use.

---

*Crafted for aspiring Python Backend Developers — Happy Coding! 🐍🚀*
