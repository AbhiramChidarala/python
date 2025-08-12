#collections = single "variable" that can hold multiple items
#  List = [] ordered and changeable, allows duplicate items
#  Tuple = () ordered and unchangeable, allows duplicate items
#  Set = {} unordered and unindexed, no duplicate items, but Add/ Remove Ok.

fruits = {"apple", "banana","watermelon", "cherry", "orange", "kiwi"}
#print(fruits[2])  # Accessing the third item

#print(dir(fruits))  # List of methods available for the list object

#print(help(fruits))  # gives a clear description for the list object

#print(len(fruits))  # Length of the list

#print("apple" in fruits)  # Check if "apple" is in the list gives in boolean value (True/False)
#print("grape"  in fruits)  # Check if "grape" is not in the list gives in boolean value (True/False)

#fruits[0] = "mango"  # Change the first item

#for fruit in fruits:
#    print(fruit)  # Print each item in the list

#fruits.append("grape")  # Add an item to the end of the list
#fruits.insert(0,"watermelon")  # Insert an item at the beginning of the list")
#fruits.remove("banana")  # Remove an item from the list
#fruits.pop()  # Remove the last item from the list
#fruits.sort()  # Sort the list in alphabetical order
#fruits.reverse()  # Reverse the order of the list
#fruits.clear()  # Clear the list (remove all items)


#print(fruits.index("kiwi"))  # Find the index of "kiwi" in the list
print(fruits)