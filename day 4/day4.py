#create lists
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = ["alice", 42, 3.14, True]

#access by index
print(fruits[0])  # Output: apple
print(fruits[-1])  # Output: cherry

#slicing
print(fruits[1:3])  # Output: ['banana', 'cherry']

#list methods
fruits.append("orange")
fruits.remove("banana")
fruits.insert(1, "grape")
print(len(fruits))  # Output: 4
print(fruits)  # Output: ['apple', 'grape', 'cherry', 'orange']


#loop through list
for fruit in fruits:
    print(fruit)

    #list with numbers
    scores = [85, 90, 78, 92, 88]
    print(max(scores))  # Output: 92
    print(min(scores))  # Output: 78
    print(sum(scores))  # Output: 433
