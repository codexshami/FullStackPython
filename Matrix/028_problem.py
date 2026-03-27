#Add two matrics
def add_matrices(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Matrices must have the same dimensions")
    
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    
    return result
# Get input for the first matrix
rows1 = int(input("Enter the number of rows for the first matrix: "))
cols1 = int(input("Enter the number of columns for the first matrix: "))
matrix1 = []
print("Enter the elements of the first matrix:")
for i in range(rows1):
    row = list(map(int, input().split()))
    matrix1.append(row)
# Get input for the second matrix
rows2 = int(input("Enter the number of rows for the second matrix: "))
cols2 = int(input("Enter the number of columns for the second matrix: "))
matrix2 = []
print("Enter the elements of the second matrix:")
for i in range(rows2):
    row = list(map(int, input().split()))
    matrix2.append(row)
# Add the two matrices and print the result
try:
    result = add_matrices(matrix1, matrix2)
    print("Result of adding the two matrices:")
    for row in result:
        print(row)
except ValueError as e:
    print(e)
#Logic for interview


def add_matrices(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Matrices must have the same dimensions")
    
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    
    return result
# Get input for the first matrix
rows1 = int(input("Enter the number of rows for the first matrix: "))
cols1 = int(input("Enter the number of columns for the first matrix: "))
matrix1 = []
print("Enter the elements of the first matrix:")
for i in range(rows1):
    row = list(map(int, input().split()))
    matrix1.append(row)
# Get input for the second matrix
rows2 = int(input("Enter the number of rows for the second matrix: "))
cols2 = int(input("Enter the number of columns for the second matrix: "))
matrix2 = []
print("Enter the elements of the second matrix:")
for i in range(rows2):
    row = list(map(int, input().split()))
    matrix2.append(row)
# Add the two matrices and print the result
try:    
    result = add_matrices(matrix1, matrix2)
    print("Result of adding the two matrices:")
    for row in result:
        print(row)  
except ValueError as e:
    print(e)
    
#time complexity: O(m*n) where m is the number of rows and n is the number of columns in the matrices, because we need to iterate through each element of the matrices once to perform the addition. The space complexity is O(m*n) because we are creating a new matrix to store the result, which has the same dimensions as the input matrices.