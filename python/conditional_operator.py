#CONDITIONAL OPERATOR =  A ONE LINE SHORT CUT FOR THE IF-ELSE STATEMENT
#                        PRINT OR ASSIGN ONE OF TWO VALUE BASED ON CONDITION 
#                        X IF CONDITION ELSE Y
#num = 69
#print("positive" if  num > 0 else "negative")

#result = "even" if num % 2 == 0 else "odd"

#print(result)


age = int(input("Enter the age :"))

result = "Adult" if age >18 else "child"

print(result)

temp = float(input("Enter the temperature :"))

weather = "sunny" if temp > 25 else "cold"

print(weather)

a = int(input("Enter the number :"))
b = int(input("Enter the number :"))

add = a if a > b else b

print(add)