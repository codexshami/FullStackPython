#Multiply two matrices A and B.
def multiply_matrices(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix")
    
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            sum_product = 0
            for k in range(len(matrix1[0])):
                sum_product += matrix1[i][k] * matrix2[k][j]
            row.append(sum_product)
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
# Multiply the two matrices and print the result
try:
    result = multiply_matrices(matrix1, matrix2)
    print("Result of multiplying the two matrices:")
    for row in result:
        print(row)
except ValueError as e:
    print(e)
#Logic for interview
def multiply_matrices(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix")
    
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            sum_product = 0
            for k in range(len(matrix1[0])):
                sum_product += matrix1[i][k] * matrix2[k][j]
            row.append(sum_product)
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
# Multiply the two matrices and print the result
try:   
    result = multiply_matrices(matrix1, matrix2)
    print("Result of multiplying the two matrices:")
    for row in result:
        print(row)
except ValueError as e:
    print(e)
# The time complexity of this algorithm is O(n*m*p) where n is the number of rows in the first matrix, m is the number of columns in the first matrix (which is also the number of rows in the second matrix), and p is the number of columns in the second matrix. The space complexity is O(n*p) for storing the result matrix.