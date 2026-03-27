# Solution 20: Chaos Tracker

## Approach Explanation
We can count inversions while sorting the array using Merge Sort. During the "merge" step, if an element from the right subarray is chosen, it means it is smaller than all remaining elements in the left subarray. Each such occurrence adds `len(left_remaining)` to the inversion count.

## Step-by-Step Logic
1. Implement a modified merge sort that returns both the sorted array and the inversion count.
2. In the `merge` function:
   - If `left[i] <= right[j]`: Add `left[i]` to result.
   - If `left[i] > right[j]`: Add `right[j]` to result and increment `count` by `len(left) - i`.
3. Recursion: `total_count = left_count + right_count + merge_count`.
4. Return `total_count`.

## Complexity
- **Time Complexity:** O(N log N), same as merge sort.
- **Space Complexity:** O(N), for merging temporary arrays.

## Code
```python
def count_inversions(arr):
    def merge_and_count(a):
        if len(a) <= 1:
            return a, 0
            
        mid = len(a) // 2
        left, left_c = merge_and_count(a[:mid])
        right, right_c = merge_and_count(a[mid:])
        
        merged = []
        i = j = count = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                # Fundamental inversion logic
                count += len(left) - i
                j += 1
                
        merged.extend(left[i:])
        merged.extend(right[j:])
        
        return merged, left_c + right_c + count

    _, total_inversions = merge_and_count(arr)
    return total_inversions
```
