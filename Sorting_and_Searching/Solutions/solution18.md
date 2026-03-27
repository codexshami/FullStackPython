# Solution 18: Cardinal Comparison (Count of Smaller Numbers After Self)

## Approach Explanation
This problem can be solved by modifying the Merge Sort algorithm. During the merge step, when an element from the right half is smaller than an element from the left half, it means all the remaining elements in the left half will have this right element as a "smaller to the right" occurrence.
Alternatively, we store the number of elements moved from right to left while merging.

## Step-by-Step Logic
1. Create a list of tuples `(value, original_index)`.
2. Perform Merge Sort on this list.
3. During `merge(left, right)`:
   - Use a pointer `j` for the right half.
   - For each element in the left half, count how many elements from the right half are smaller than it.
   - Update `res[original_index]` with this count.
4. Note that we need to maintain the "running sum" of smaller elements found in previous merges during the recursive process.

## Complexity
- **Time Complexity:** O(N log N).
- **Space Complexity:** O(N).

## Code
```python
def count_smaller(nums):
    n = len(nums)
    res = [0] * n
    indices = list(range(n))
    
    def sort(l, r):
        if r - l <= 1: return
        
        mid = (l + r) // 2
        sort(l, mid)
        sort(mid, r)
        
        # Merge step
        temp = []
        i, j = l, mid
        while i < mid or j < r:
            if j == r or (i < mid and nums[indices[i]] <= nums[indices[j]]):
                res[indices[i]] += (j - mid)
                temp.append(indices[i])
                i += 1
            else:
                temp.append(indices[j])
                j += 1
        indices[l:r] = temp
        
    sort(0, n)
    return res
```
