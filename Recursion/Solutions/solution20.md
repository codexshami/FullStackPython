# Solution 20: The Sorted Merge (Merge Sort)

## Approach Explanation
Merge Sort divides the array in half, recursively sorts each half, then merges the two sorted halves into one sorted array.

## Step-by-Step Logic
1. Base case: If the array has 0 or 1 elements, it's already sorted — return it.
2. Find the middle index.
3. Recursively sort the left half and the right half.
4. Merge the two sorted halves using a two-pointer merge technique.

## Complexity
- **Time Complexity:** O(N log N).
- **Space Complexity:** O(N).

## Code
```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```
