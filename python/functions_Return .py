#functions = A block of reusable code 
#             place() after the function name to invoke it 

#def happy_birthday(name, age ):
#    print(f"Happy Birthday {name}!")
#    print(f"You are {age} years old ")
#    print("Happy Birthday to You")
#    print()

#happy_birthday("Murali", 20)  # This calls the happy_birthday function
#happy_birthday("Leo Das", 25)  
#happy_birthday("AbhiRam", 30)  

# Return = it is a statement used to end a function and send the result back to the caller


def  create_name(first , last):
    first = first.capitalize()
    last =  last.capitalize()
    return first + " " + last 

full_name = create_name("Avengers", "Doomsday")

print(full_name)  # Output: Avengers Doomsday