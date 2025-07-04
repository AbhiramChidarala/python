#apple = 5
 
#apple =apple +1
#apple += 1
#apple = apple -2
#apple -= -2
#apple =apple *5
#apple *= 4
#apple = apple / 10
#apple /= 5
#apple = apple **2
#apple **= 3

#print(apple)


#---------------------------------------------------------------------------------------
                #Mathmatical operators

#x = 3.14
#y = 4
#z = 9
#result = round(x)                  # round oprators
#result = abs(z)                    # absoute oprator = find the distance of a number from 0
#result = pow(4 , 2)                #power oprator = find the power of the variabe 
#result =  max(x, y,z)              #max oprator = finds the max value between the variables 
#result = min(x,y,z)                 #min oprator  = finds the min value between the variables 
#print(result)


#------------------------------------------------------------------------------------------------
                        #find the constant value in mathematics
#import math

#print(math.pi)              # math.pi used to find the value of pi
#print(math.e)               # math.e to find the value of e

#x = 64 
#result = math.sqrt(x)       #math.sqrt used to find the square root of the value

#print(result)

#y = 10.2

#math = math.ceil(y)        #math.ceil used to up the floating value 

#print(math)

#------------------------------------------------------------------------------
                            #EXAMPLE#
# CIRCUMFERENCE OF CIRCLE 
#import math

#radius = float(input("Enter the radius of a circle : "))

#circumference = 2 * math.pi* radius

#print(f"the circumference of the circle {circumference}")

# 2nd EXAMPLE  AREA OF CIRCLE 
#import math 

#radius = float(input("Enter the radius of the circle : "))

#area = math.pi * pow(radius, 2)

#print(f"The area of circle is {area}")

#EXAMPLE 3

import math

a = float(input("Enter the side A :"))
b = float(input("Enter the side B :"))

c = math.sqrt(pow(a,2)+ pow(b,2))

print(c)