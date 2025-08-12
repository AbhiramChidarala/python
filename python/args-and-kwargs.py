# *args = allows you to pass mulitple non key arguments
# **kwargs = allows you to pass multiple keyword - arguments
#              '*' unpacking operator 
#               1. positional 2. default 3. keyword 4. ARBITRARY
# arbitrary arguments means a varying amount of arguments.
# *args means argumnets and **kwargs means keyword arguments



#def add(*args):             #we can change the *args to any name
#    total = 0
#    for arg in  args:
#        total += arg 
#    return total 

#print(add(1,2,3,4))

#def display_name(*args):
#    for arg in args:
#        print(arg, end= "" )
#
#display_name("MR.","Peter","Parker")

def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(street = "subedari",
              city = "hanamkonda",
              state = "teleangana",
              postal_code = "506001")