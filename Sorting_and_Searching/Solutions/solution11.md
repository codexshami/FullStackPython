# Solution 11: Divide and Merge Sort

## Approach Explanation
1. Divide: Split the array into two halves.
2. Conquer: Recursively sort both halves.
3. Combine: Merge the two sorted halves into one sorted array.

## Step-by-Step Logic
1. Base case: If array length <= 1, return array.
2. Find `mid` and split into `left` and `right` halves.
3. Call `merge_sort` on both halves.
4. Merge function:
   - Use two pointers to compare elements of `left` and `right`.
   - Append the smaller one to the result.
   - Append any remaining elements.

## Complexity
- **Time Complexity:** O(N log N) in all cases.
- **Space Complexity:** O(N) for the temporary lists.

## Code
```python
def merge_sort(nums):
    if len(nums) <= 1:
        return nums
        
    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    
    return merge(left, right)

def merge(left, right):
    res = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
            
    res.extend(left[i:])
    res.extend(right[j:])
    return res
```
