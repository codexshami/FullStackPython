# Solution 19: Tower Transfer (Tower of Hanoi)

## Approach Explanation
We solve the Tower of Hanoi by breaking it into three sub-problems:
1. Move `n-1` disks from source to auxiliary.
2. Move the largest disk from source to target.
3. Move `n-1` disks from auxiliary to target.

## Step-by-Step Logic
1. Base case: If `n == 1`, move disk 1 from source to target directly.
2. Recursively move `n-1` disks from source to auxiliary using target as helper.
3. Print: Move disk `n` from source to target.
4. Recursively move `n-1` disks from auxiliary to target using source as helper.

## Complexity
- **Time Complexity:** O(2^N - 1) moves.
- **Space Complexity:** O(N) (recursion stack).

## Code
```python
def tower_of_hanoi(n, source='A', target='C', auxiliary='B'):
    if n == 1:
        print(f"Move disk 1 from Rod {source} to Rod {target}")
        return
    
    tower_of_hanoi(n - 1, source, auxiliary, target)
    print(f"Move disk {n} from Rod {source} to Rod {target}")
    tower_of_hanoi(n - 1, auxiliary, target, source)
```
