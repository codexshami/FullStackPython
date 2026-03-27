# Solution 6: Distributed Multiplication

## Approach Explanation
We can solve this by calculating the prefix products and the suffix products. For any element at index `i`, its result is `(product of all elements to its left) * (product of all elements to its right)`.

## Step-by-Step Logic
1. Initialize an `answer` array of the same length as `nums`, filled with 1s.
2. Initialize `prefix = 1`. Iterate from left to right:
   - `answer[i] = prefix`
   - `prefix *= nums[i]`
3. Now `answer[i]` contains the product of all elements to the left of `i`.
4. Initialize `suffix = 1`. Iterate from right to left:
   - `answer[i] *= suffix`
   - `suffix *= nums[i]`
5. Now `answer[i]` contains the product of all elements except `nums[i]`.

## Complexity
- **Time Complexity:** O(N), two passes over the array.
- **Space Complexity:** O(1) if we don't count the output array, otherwise O(N).

## Code
```python
def product_except_self(nums):
    n = len(nums)
    answer = [1] * n
    
    # Prefix product
    prefix = 1
    for i in range(n):
        answer[i] = prefix
        prefix *= nums[i]
        
    # Suffix product combined with the result
    suffix = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= suffix
        suffix *= nums[i]
        
    return answer
```
