# Solution 12: Celestial Impact

## Approach Explanation
We use a stack to process asteroids one by one. Collisions only happen when a left-moving asteroid (negative) meets a right-moving asteroid (positive) that is already in the stack.

## Step-by-Step Logic
1. Initialize an empty `stack`.
2. Iterate through each `asteroid` in `asteroids`:
   - While stack is not empty and `asteroid < 0` and `stack[-1] > 0`:
     - If `abs(asteroid) > stack[-1]`: pop the surviving right-moving asteroid and continue check.
     - If `abs(asteroid) == stack[-1]`: pop the right-moving and set current to "exploded".
     - If `abs(asteroid) < stack[-1]`: current asteroid "explodes".
   - If current asteroid didn't explode, push it to stack.
3. Return stack.

## Complexity
- **Time Complexity:** O(N), each asteroid is pushed/popped at most once.
- **Space Complexity:** O(N).

## Code
```python
def asteroid_collision(asteroids):
    stack = []
    
    for a in asteroids:
        # Collision loop
        while stack and a < 0 and stack[-1] > 0:
            diff = a + stack[-1]
            if diff < 0:
                stack.pop() # right-moving asteroid explodes
                continue
            elif diff == 0:
                stack.pop() # both explode
            # If diff > 0, incoming left-moving asteroid (a) explodes
            break
        else:
            # Executes if loop finished without 'break'
            # (i.e., NO collision happened or incoming asteroid survived all)
            if not stack or a > 0 or stack[-1] < 0:
                stack.append(a)
                
    return stack
```
