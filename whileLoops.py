#while loops = execute some code while a condition is true
# while loops are used to repeat a block of code as long as a condition is true

#name = input("Enter your name: ")

#while name == "":
#    print("you must enter a name")
#    name = input("Enter your name: ")
#print(f"Hello {name}!")

age = int(input("Enter your age "))

while age < 18:
    print("Age cannot be negative")
    age = int(input("Enter your age "))
print(f"You are {age} years old")                                       