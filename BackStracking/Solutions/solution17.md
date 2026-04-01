# Solution 17: The IP Restorer (Restore IP Addresses)

## Approach Explanation
We try placing dots at every valid position. Each segment must be 1-3 digits, between 0-255, and must not have leading zeros (except for "0" itself).

## Step-by-Step Logic
1. Use backtracking with the current index and the number of segments formed.
2. At each step, try substrings of length 1, 2, and 3.
3. Validate each segment (0-255, no leading zeros).
4. When 4 segments are formed and all characters are used, save the IP.

## Complexity
- **Time Complexity:** O(1) — bounded by the fixed max length of IP addresses.
- **Space Complexity:** O(1).

## Code
```python
def restore_ip_addresses(s):
    result = []
    
    def backtrack(start, segments):
        if len(segments) == 4 and start == len(s):
            result.append('.'.join(segments))
            return
        if len(segments) == 4 or start == len(s):
            return
        
        for length in range(1, 4):
            if start + length > len(s):
                break
            segment = s[start:start + length]
            if (segment[0] == '0' and len(segment) > 1) or int(segment) > 255:
                continue
            backtrack(start + length, segments + [segment])
    
    backtrack(0, [])
    return result
```
