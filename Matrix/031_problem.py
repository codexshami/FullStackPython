#Find the sum of the diogonal elements of a square matrix
def diagonal_sum(matrix):
    total = 0
    for i in range(len(matrix)):
        total += matrix[i][i]  # Add the primary diagonal element
        total += matrix[i][len(matrix) - 1 - i]  # Add the secondary diagonal element
    if len(matrix) % 2 == 1:  # If the matrix has an odd number of rows/columns, subtract the middle element (which was added twice)
        total -= matrix[len(matrix) // 2][len(matrix) // 2]
    return total
# Get input for the matrix
size = int(input("Enter the size of the square matrix: "))
matrix = []
print("Enter the elements of the matrix:")
for i in range(size):
    row = list(map(int, input().split()))
    matrix.append(row)
# Calculate the sum of the diagonal elements and print the result
result = diagonal_sum(matrix)
print("The sum of the diagonal elements is:", result)

#Logic for interview
def diagonal_sum(matrix):
    total = 0
    for i in range(len(matrix)):
        total += matrix[i][i]  # Add the primary diagonal element
        total += matrix[i][len(matrix) - 1 - i]  # Add the secondary diagonal element
    if len(matrix) % 2 == 1:  # If the matrix has an odd number of rows/columns, subtract the middle element (which was added twice)
        total -= matrix[len(matrix) // 2][len(matrix) // 2]
    return total
# Get input for the matrix
size = int(input("Enter the size of the square matrix: "))
matrix = []
print("Enter the elements of the matrix:")
for i in range(size):
    row = list(map(int, input().split()))
    matrix.append(row)
# Calculate the sum of the diagonal elements and print the result
result = diagonal_sum(matrix)
print("The sum of the diagonal elements is:", result)
#time complexity: O(n) where n is the size of the matrix, because we need to iterate through the diagonal elements of the matrix once. The space complexity is O(1) because we are using a constant amount of extra space.