# Solution 20: Dual-Stream Optimization

## Approach Explanation
Since the arrays are sorted, the smallest sum is always `nums1[0] + nums2[0]`. We use a Min-Heap to explore potential pairs. We start with pairs `(nums1[i], nums2[0])` for all `i` (up to `k`). When we pop a pair `(nums1[i], nums2[j])`, the next candidate from that `nums1` element is `(nums1[i], nums2[j+1])`.

## Step-by-Step Logic
1. Initialize a Min-Heap.
2. Push `(nums1[i] + nums2[0], i, 0)` for `i` from 0 to `min(len(nums1), k) - 1`.
3. While `k > 0` and heap is not empty:
   - Pop `(sum, i, j)`.
   - Add `[nums1[i], nums2[j]]` to result.
   - If `j + 1 < len(nums2)`, push `(nums1[i] + nums2[j+1], i, j+1)` to heap.
   - Decrement `k`.
4. Return result.

## Complexity
- **Time Complexity:** O(K log K).
- **Space Complexity:** O(K).

## Code
```python
import heapq

def k_smallest_pairs(nums1, nums2, k):
    if not nums1 or not nums2: return []
    
    h = []
    # Initial candidates: (sum, index_in_nums1, index_in_nums2)
    for i in range(min(len(nums1), k)):
        heapq.heappush(h, (nums1[i] + nums2[0], i, 0))
        
    res = []
    while h and k > 0:
        val, i, j = heapq.heappop(h)
        res.append([nums1[i], nums2[j]])
        
        if j + 1 < len(nums2):
            heapq.heappush(h, (nums1[i] + nums2[j+1], i, j + 1))
            
        k -= 1
        
    return res
```
