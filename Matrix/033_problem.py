#find the determinant of a matrix
def determinant(matrix):
    if len(matrix) != len(matrix[0]):
        raise ValueError("Matrix must be square")
    
    n = len(matrix)
    
    if n == 1:
        return matrix[0][0]
    
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    det = 0
    for j in range(n):
        sub_matrix = [row[:j] + row[j+1:] for row in matrix[1:]]
        det += ((-1) ** j) * matrix[0][j] * determinant(sub_matrix)
    
    return det
# Get input for the matrix
size = int(input("Enter the size of the square matrix: "))
matrix = []
print("Enter the elements of the matrix:")
for i in range(size):
    row = list(map(int, input().split()))
    matrix.append(row)
# Calculate the determinant and print the result
try:    
    result = determinant(matrix)
    print("The determinant of the matrix is:", result)
except ValueError as e:
    print(e)

#Logic for interview
def determinant(matrix):
    if len(matrix) != len(matrix[0]):
        raise ValueError("Matrix must be square")
    
    n = len(matrix)
    
    if n == 1:
        return matrix[0][0]
    
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    det = 0
    for j in range(n):
        sub_matrix = [row[:j] + row[j+1:] for row in matrix[1:]]
        det += ((-1) ** j) * matrix[0][j] * determinant(sub_matrix)
    
    return det
# Get input for the matrix
size = int(input("Enter the size of the square matrix: "))
matrix = []
print("Enter the elements of the matrix:")
for i in range(size):
    row = list(map(int, input().split()))
    matrix.append(row)
# Calculate the determinant and print the result
try:    
    result = determinant(matrix)
    print("The determinant of the matrix is:", result)
except ValueError as e:
    print(e)
#time complexity: O(n!) in the worst case, because we are calculating the determinant using recursion and the number of operations grows factorially with the size of the matrix. The space complexity is O(n) due to the recursive call stack.