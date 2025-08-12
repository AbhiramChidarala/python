#Nested Loops = A loop inside another loop.(outer, inner)
#           outerloop: 
#              innerloop:
rows = int(input("Enter the no.of rows: "))
cols = int(input("Enter the no.of columns: "))
symbol = input("Enter the symbol to print:")

for x in range (rows):
    for y in range(cols):
        print(symbol, end=" ")
    print()         # This code will print a rectangle of the specified rows and columns using the given symbol.
