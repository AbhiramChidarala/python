#PYTHON CALCULATOR

operator = input("Enter the operator (+,-,*,/ ) :")
num1 = float(input("Enter the 1st number :"))
num2 = float(input("Enter the 2nd number :"))

if operator == "+":
    result = num1+num2
    print(round(result,3))                  # round used for round offing the decimals
elif operator =="-":
    result = num1-num2
    print(round(result,3))
elif operator == "*":
    result = num1*num2
    print(round(result,3))
elif operator == "/":
    result = num1/num2
    print(round(result,3))
else:
    print(f" {operator} enter the correct operator")
