#check if a matrix is symmatric
def is_symmetric(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True
# Get input for the matrix
rows = int(input("Enter the number of rows for the matrix: "))
cols = int(input("Enter the number of columns for the matrix: "))
matrix = []
print("Enter the elements of the matrix:")

for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)
# Check if the matrix is symmetric and print the result
if is_symmetric(matrix):
    print("The matrix is symmetric.")
else:
    print("The matrix is not symmetric.")

#Logic for interview
def is_symmetric(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != matrix[j][i]:  # Check if the element at position (i, j) is equal to the element at position (j, i)
                return False  # If any pair of elements does not match, the matrix is not symmetric
    return True  # If all pairs of elements match, the matrix is symmetric
# Get input for the matrix
rows = int(input("Enter the number of rows for the matrix: "))
cols = int(input("Enter the number of columns for the matrix: "))
matrix = []
print("Enter the elements of the matrix:")
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)
# Check if the matrix is symmetric and print the result
if is_symmetric(matrix):
    print("The matrix is symmetric.")
else:
    print("The matrix is not symmetric.")
#time complexity: O(n*m) where n is the number of rows and m is the number of columns in the matrix, because we need to check each element of the matrix. The space complexity is O(1) because we are using a constant amount of extra space.