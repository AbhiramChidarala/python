import numpy as np

#array = np.array('A')
# to find the number of dimensions in array 
#print(array)

# every array elements has to be equal EX :- one array has 3 elements and another has 2 elements 
# then it is a error 

#print(array.ndim)  

#print(array.shape) # to find the row, columns and height of the array 

#print(array[0][0][0])           # chain indexing in python  to find the elements in array

#  Multidimensional indexing in NumPy allows for precise selection and manipulation of elements within N-dimensional arrays.
#  Unlike Python lists, NumPy arrays support direct multidimensional indexing 
#  using a single set of square brackets and comma-separated indices for each dimension.

array = np.array([[['A','B','C'],['D','E','F'],['G','H','I']],
                  [['J','K','L'],['M','N','O'],['P','Q','R']],
                  [['S','T','U'],['V','W','X'],['Y','Z',' ']]])


#print(array[0,0,2])

word = array[1,1,0] + array [2,0,2] + array[1,2,2] + array[0,0,0] + array[1,0,2] + array[0,2,2]

print(word)