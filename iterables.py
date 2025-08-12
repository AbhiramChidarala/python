#Iterables = An object/collection that can return its elements 
#            one at a time , allowing it to be iterated over in a loop.


#fruits = {"Apple", "orange","banana"}   #iterables can be done using tuples and sets 

#for items in fruits:
#    print(items)

#name = "MURALI"     # iterables can be done with strings arguments 

#for items in name:
#    print(items,end=" ")

# now performing iterables using dictionary

my_dictionary = {"A": 1,"B":2,"C":3,"D":4}

for key, value in my_dictionary.items():
    print(f"{key}: {value}")