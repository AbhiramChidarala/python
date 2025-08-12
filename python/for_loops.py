#for Loops = execute a block of code a number of times
# for loops are used to repeat a block of code a specific number of times
# you can iterate over a sequence (like a list, tuple, or string) or a range of numbers

#for x in range (1,11):          # find the range between the numbers 1 and 10
#    print(x)

#for year in reversed(range(1,11)):          #find the range between the numbers 1 and 10 in reverse order
#    print(year)
#print("HAPPY NEW YEAR 2024!")

#for x in range(1, 11 , 3):  # find the range between the numbers 1 and 10 with a step of 3
#    print(x)

for x in range(1,21):
    if x == 13:
        continue            # skip the number 13 using continue
    print(x)
print("------------------------------------------------------------------------------------")
for y in range (1,21):
    if y == 13:
        break               # stop the loop when it reaches 13 using break
    print(y)