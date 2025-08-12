# LOGICAL OPERATOR =  EVALUATE MULITPLE CONDITIONS  (OR, AND , NOT )
#                     OR  = AT LEAST ONE CONDITIONS MUST BE TRUE
#                     AND = BOTH CONDITIONS MUST BE TRUE 
#                     NOT  = INVERTS THE CONDITONS (NOT TRUE, NOT FALSE)


#---------------------OR OPERATOR--------------------------
#temp = 50
#is_raining = Fals
#if temp > 35 or temp < 0 or is_raining:
#        print("Outdoor event is cancelled")
#else:
#        print("Outdoor even is still scheduled")
#------------------AND OPERATOR---------------------------- 
'''
temp = 20
is_sunny = True

if temp>=28 and is_sunny :
    print("Temperature is hot")
    print("And it is a sunny day")
elif temp<=0 and is_sunny:
    print("Temperature is cold")
    print("and is a sunny day ")
elif 28 > temp > 0 and is_sunny:
    print("Temperature is warm outside")
    print('And is  a sunny day ')
'''
#------------------NOT OPERATOR--------------------------
temp = 0
is_sunny = False

if temp>=28 and is_sunny :
    print("Temperature is hot")
    print("And it is a sunny day")

elif temp<=0 and is_sunny:
    print("Temperature is cold")
    print("and is a sunny day ")

elif 28 > temp > 0 and is_sunny:
    print("Temperature is warm outside")
    print('And is  a sunny day ')

elif temp>=28 and  not is_sunny :
    print("Temperature is hot")
    print("And it is a raining")

elif temp<=0 and is_sunny:
    print("Temperature is cold")
    print("and is a raining ")
    
elif 28 > temp > 0 and is_sunny:
    print("Temperature is warm outside")
    print('And is  a raining ')