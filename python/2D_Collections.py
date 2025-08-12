 # we can also create a tuple using 2D collections


#fruits =     ["apple", "banana","orange","kiwi"]
#vegetables = ["carrot", "broccoli", "spinach"]
#meats =      ["chicken", "fish", "turkey"]

#list_of_items = [fruits, vegetables, meats]

#print(list_of_items)  # Print the list of lists

#print(list_of_items[1][2])  # Accessing the third item in the second list (vegetables)


#grocery_list = [ ["apple(1)", "banana(2)","orange(3)"],
#                 ["carrot(4)", "broccoli(5)", "spinach(6)"],
#                 ["chicken(7)", "fish(8)", "turkey(9)"]      ]
#
#for collection in grocery_list:
#    for food in collection:
#        print(food, end="  ")
#   print()  # Print each item in the grocery list with a space in between

#---------------------------------------2D COLLECTIONS -----------------------------------
# Sample number pad design using 2D collections

num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))

for row in num_pad:
    for num in row:
        print(num, end="  ")
    print()  # Print each row of the number pad with a space in between