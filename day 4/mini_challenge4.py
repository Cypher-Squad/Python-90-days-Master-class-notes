#Create a shopping cart as a list. Add 3 items, remove 1, and print the final cart with total item count.
#1. create a shopping cart as a list
shopping_cart = []
#2. add 3 items to the cart
shopping_cart.append("Apple")
shopping_cart.append("Banana")
shopping_cart.append("Orange")
#3. remove 1 item from the cart
shopping_cart.remove("Banana")
#4. print the final cart with total item count
print("Final Shopping Cart:", shopping_cart)  # Output: Final Shopping Cart: ['Apple
#', 'Orange']
print("Total Item Count:", len(shopping_cart))  # Output: Total Item Count: 2