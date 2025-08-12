# PYTHON WEIGHT CONVERTER

weight = float(input("Enter your weight :  "))
unit = input("KiloGrams or Pounds (K or L):")

if unit =="K":
    weight = weight * 2.205
    unit = "Lbs"
elif unit == "L":
    weight = weight / 2.205
    unit = "kgs"
else: 
    print(f"{unit} was not valid")

print(f"Your weight is : {weight} {unit}")