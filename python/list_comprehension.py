# List Comprehension = A concise way to create lists in python 
#                      compact and easier to read then traditional loops 
#                      [expression for value in iterable if condition]

#doubles = [x * 2 for x in range(1,11)]

#print(doubles)

#triples = [x *3 for x in range(1,11)]
#squares = [z* z for z in range(1,16)]
#print(squares)

#fruits = ["apple","banana","orange","kiwi"]

#uppercase_fruits = [fruit.upper() for fruit in fruits]
#first_letter = [fruit[0] for fruit in fruits]
#print(first_letter)

numbers = [1,2,-1,-3,4,5,-5,-6,8,10]

positive_nums = [num for num in numbers if num>=0]
negative_nums = [num for num in numbers if num<0]
even_nums = [num for num in numbers if num % 2 == 0]
odd_nums = [num for num in numbers if num % 2 == 1]
print(even_nums)
print(odd_nums)
print(positive_nums)
print(negative_nums)