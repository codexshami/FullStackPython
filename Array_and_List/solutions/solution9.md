# Solution 9: Consecutive Sequence Discovery

## Approach Explanation
We use a Hash Set to store all numbers. For each number, we only start counting the length of the sequence if it is the "start" of a sequence (i.e., `num - 1` is not in the set). This ensures each element is visited only twice.

## Step-by-Step Logic
1. Create a set `num_set` from the array `nums`.
2. Initialize `longest_streak = 0`.
3. Iterate through each `num` in the `num_set`:
   - Check if `num - 1` is not in `num_set`.
   - If it's not, it's the start of a sequence.
   - Set `current_num = num` and `current_streak = 1`.
   - While `current_num + 1` is in `num_set`, increment `current_num` and `current_streak`.
   - Update `longest_streak = max(longest_streak, current_streak)`.
4. Return `longest_streak`.

## Complexity
- **Time Complexity:** O(N), because each number is processed exactly twice (once when building the set and once inside the loop).
- **Space Complexity:** O(N), for the hash set.

## Code
```python
def longest_consecutive(nums):
    num_set = set(nums)
    longest_streak = 0
    
    for num in num_set:
        # Only start if it is the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1
            
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1
                
            longest_streak = max(longest_streak, current_streak)
            
    return longest_streak
```
