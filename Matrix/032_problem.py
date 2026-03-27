#rotate a matrix by 90 degrees
def rotate_matrix(matrix):
    n = len(matrix)
    # Create a new matrix with swapped dimensions
    rotated = [[0] * n for _ in range(n)]
    # Fill the rotated matrix
    for i in range(n):
        for j in range(n):
            rotated[j][n - 1 - i] = matrix[i][j]
    return rotated

# Get input for the matrix
rows = int(input("Enter the number of rows for the matrix: "))
cols = int(input("Enter the number of columns for the matrix: "))
matrix = []
print("Enter the elements of the matrix:")
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

# Rotate the matrix and print the result
rotated_matrix = rotate_matrix(matrix)
print("The rotated matrix is:")
for row in rotated_matrix:
    print(*row)

#time complexity: O(n*m) where n is the number of rows and m is the number of columns in the matrix, because we need to iterate through each element of the matrix once. The space complexity is O(n*m) because we are creating a new matrix to store the rotated elements. 