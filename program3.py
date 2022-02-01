# Consider the following example of a 3x4 matrix implemented as a list of 3 lists of length.
# For example:
# 	Input:
#  [
#    [1, 2, 3, 4],
#    [5, 6, 7, 8],
#    [9, 10, 11, 12],
#  ]

# Output:
# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

print("****** Here you can create 3x4 matrix ******")

matrix = []
new_matrix = []

for i in range(1,4): 
    print(f"you can input element for {i} row")
    row = []  
    row.clear()
    for j in range(1,5):   
        element = int(input(f'Enter a value for {j} element: '))
        row.append(element)
    matrix.append(row)

print('Before :',matrix)

for i in range(4):
    row = []
    row.clear()
    for j in matrix:  
        row.append(j[i])
    new_matrix.append(row)
        
print('After :',new_matrix)
       
    

