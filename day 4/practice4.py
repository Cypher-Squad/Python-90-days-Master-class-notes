#1. create list of city
cities = ["New York", "London", "Paris", "Tokyo"]
print(cities[0])  # Output: New York
print(cities[-1])  # Output: Tokyo

#2. add new city to the list
cities.append("Sydney")
print(cities)  # Output: ['New York', 'London', 'Paris', '
Tokyo', 'Sydney']

#3. remove a city from the list
cities.remove("Paris")

#4. find the total of cities in the list sing len() function
print(len(cities))  # Output: 4

#5. loop through a list of names and print "hello, {name}!"
names = ["Alice", "Bob", "Charlie"]
for name in names:
    print(f"hello, {name}!")
