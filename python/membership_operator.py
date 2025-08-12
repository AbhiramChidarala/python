#Mermbership operator = used to test whether a value or variable is found 
#                       in a sequence (string,list , tuple, set, or dictionary)
#                           1.in        2. not in


word = "MURALIDHAR"

letter = input("Guess a letter in serect word : ")

if letter  not in word: 
    print(f"{letter} is not found in word ")
else:
    print(f"{letter} found in word")
    