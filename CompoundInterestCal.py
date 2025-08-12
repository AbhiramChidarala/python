#Python Code to calculate Compound Interest

principal = 0
rate = 0
time = 0

while principal <= 0:
    principal = float(input("Enter the principal amount (greater than 0): "))
    if principal <= 0:
        print("Principal must be greater than 0. Please try again.")
while rate <= 0:
    rate = float(input("Enter the rate of interest (greater than 0): "))
    if rate <= 0:
        print("Rate must be greater than 0. Please try again.")

while time <= 0:
    time = float(input("Enter the time period in years (greater than 0): "))
    if time <= 0:
        print("Time must be greater than 0. Please try again.")

total = principal*pow((1+rate/100),time)
print(f"The total amount after {time} years is: {total:.2f}")
