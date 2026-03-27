# Solution 16: Sequential Byte Compression (String Compression)

## Approach Explanation
We use two pointers: `read` to iterate through the original array and `write` to update the array in-place.

## Step-by-Step Logic
1. `write = 0`, `i = 0`.
2. While `i < len(chars)`:
   - `char = chars[i]`, `count = 0`.
   - While `i < len(chars)` and `chars[i] == char`:
     - `i += 1`, `count += 1`.
   - `chars[write] = char`, `write += 1`.
   - If `count > 1`:
     - For each digit in `str(count)`:
       - `chars[write] = digit`, `write += 1`.
3. Return `write`.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(1).

## Code
```python
def compress(chars):
    write = 0
    i = 0
    while i < len(chars):
        char = chars[i]
        count = 0
        while i < len(chars) and chars[i] == char:
            i += 1
            count += 1
        
        chars[write] = char
        write += 1
        
        if count > 1:
            for digit in str(count):
                chars[write] = digit
                write += 1
                
    return write
```
