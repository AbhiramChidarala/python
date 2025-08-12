#---------------------------------------STRING METHODS -----------------------------------

#name = input("Enter the full name ")

#result = len(name)                  # LEN() IS USED TO FIND THE LENGTH OF THE STRING

#result = name.find("M")              # FIND() = USED TO FIND THE FIRST OCCURANCE OF THE STRING 

#result = name.rfind("A")              #RFIND() = USED TO FIND THE LAST OCCURANCE OF THE STRING 
                                     # IF THERE IS NO RESULT THE RFIND() GIVES THE NEGATIVE VALUE (-1)

#name = name.capitalize()                # CAPITALIZE = USED TO WRITE THE 1ST LETTER IN CAPITAL

#name = name.upper()                         # UPPER = CAPITALIZE ALL THE LETTERS 
#name = name.lower()                         # USED FOR LOWERING THE LETTERS

#result = name.isalpha()                      # USED TO FIND THE ALPHABETS IN THE VARIABLE 

#print(result)


#-------------------------------------------------------------------------------------
            # ALL THE STRING METHODS IN PYTHON 
#print(help(str))
#

#-------------------------------------------------------------------------------------

# 1. validate the username which is below 12 characters
# 2. username must not contain spaces 
# 3. username must not contain digits

username = input("Enter the username : ")


if len(username) > 12: 
    print("username cannot be more than 12 characters")
elif not username.find(" ") == -1:
    print("Your username doesn't contain any spaces.")
elif not username.isalpha():
    print("Your username doesn't contain numbers")
else: 
    print(f"Welcome {username}")    