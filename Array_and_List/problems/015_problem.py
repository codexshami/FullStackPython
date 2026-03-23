#rotate an array to the right by k positions
def rotate_array(arr, k):
    n = len(arr)
    k = k % n  # Handle cases where k is larger than the array length
    return arr[-k:] + arr[:-k]

# Example usage:
arr = [1, 2, 3, 4, 5]
k = 2
print(rotate_array(arr, k))  # Output: [4, 5, 1, 2, 3]
# Logic method without function:
arr = [1, 2, 3, 4, 5]
k = 2
n = len(arr)    
k = k % n  # Handle cases where k is larger than the array length
rotated_arr = arr[-k:] + arr[:-k]  # Rotate the array by slicing and concatenating the appropriate parts
print(rotated_arr)  # Output: [4, 5, 1, 2, 3]   