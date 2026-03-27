#Print a matrix in spiral order
def spiral_order(matrix):
    if not matrix:
        return []
    
    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    
    while top <= bottom and left <= right:
        # Traverse from left to right
        for j in range(left, right + 1):
            result.append(matrix[top][j])
        top += 1
        
        # Traverse from top to bottom
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1
        
        if top <= bottom:
            # Traverse from right to left
            for j in range(right, left - 1, -1):
                result.append(matrix[bottom][j])
            bottom -= 1
        
        if left <= right:
            # Traverse from bottom to top
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
    
    return result
# Get input for the matrix
rows = int(input("Enter the number of rows for the matrix: "))
cols = int(input("Enter the number of columns for the matrix: "))
matrix = []
print("Enter the elements of the matrix:")
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)
# Print the matrix in spiral order
result = spiral_order(matrix)
print("The matrix in spiral order is:", result)
#time complexity: O(n*m) where n is the number of rows and m is the number of columns in the matrix, because we need to visit each element of the matrix once. The space complexity is O(n*m) because we are storing the result in a list that can contain all elements of the matrix.