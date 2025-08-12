#Dictionary = a collection of {key :value} pairs 
#               ordered and changeable. No duplicate allowed
# A dictionary is a data structure that allows you to store data in key-value pairs.

capitals = {"usa" : "Washington D.C.",
            "india" : "New Delhi",
            "france" : "Paris",
            "germany" : "Berlin",
            "japan" : "Tokyo",}

# print(dir(capitals)) #shows all the methods and attributes of the dictionary
#print(help(capitals)) #shows the documentation of the dictionary

#print(capitals.get("india")) #returns the value of the key "india"

#if capitals.get("usa"):
#    print("that capital is in dictionary")
#else: 
#    print("That capital doesn't exist")

# Update the value in dictionary

#capitals.update({"Argentina" : "Buenos Aires"})
#capitals.update({"india" : "hyderabad"}) #updates the value of the key "india"
#print(capitals)

# delete the value in dictionary
##capitals.pop("usa") #removes the key "usa" and its value

#capitals.popitem() #removes the last added key and its value

#capitals.clear() #removes all the keys and values in the dictionary
# to get all of the keys within the dictionary but no the values 
#keys = capitals.keys()
# to get all of the values within the dictionary but no the keys
#for key in capitals.keys():
#    print(key)

# to get all of the values within the dictionary but no the keys
#values = capitals.values()

#print(values) # prints all the values in the dictionary

#for value in capitals.values():
#    print(value) # prints all the values in the dictionary

items = capitals.items() # returns a list of tuples containing the key-value pairs

for key, value in capitals.items():
    print(f"{key}: {value}")