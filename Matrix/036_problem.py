#Find the maximum sum submatrix
def max_sum_submatrix(matrix):
    if not matrix or not matrix[0]:
        return 0
    
    max_sum = float('-inf')
    rows, cols = len(matrix), len(matrix[0])
    
    for left in range(cols):
        temp = [0] * rows
        for right in range(left, cols):
            for i in range(rows):
                temp[i] += matrix[i][right]
            
            current_sum = kadane(temp)
            max_sum = max(max_sum, current_sum)
    
    return max_sum
def kadane(arr):
    max_current = max_global = arr[0]
    for i in range(1, len(arr)):
        max_current = max(arr[i], max_current + arr[i])
        if max_current > max_global:
            max_global = max_current
    return max_global
# Get input for the matrix
rows = int(input("Enter the number of rows for the matrix: "))
cols = int(input("Enter the number of columns for the matrix: "))
matrix = []
print("Enter the elements of the matrix:")
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)
# Find the maximum sum submatrix and print the result
result = max_sum_submatrix(matrix)
print("The maximum sum of a submatrix is:", result)
#time complexity: O(cols^2 * rows) because we have two nested loops for the left and right column indices, and for each pair of columns, we compute the sum of elements in the temporary array which takes O(rows) time. The space complexity is O(rows) for the temporary array used to store the sums of elements between the left and right column indices.
