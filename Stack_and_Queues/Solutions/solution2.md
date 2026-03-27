# Solution 2: Instant Minimum Access

## Approach Explanation
We maintain two stacks: one for the actual values and another for the minimum values encountered so far. When pushing a value, we push the current minimum onto the second stack.

## Step-by-Step Logic
1. `push(val)`: Always push `val` to `stack1`. For `stack2`, push `min(val, stack2[-1])` if `stack2` is not empty, otherwise push `val`.
2. `pop()`: Pop from both stacks.
3. `top()`: Return the top of `stack1`.
4. `getMin()`: Return the top of `stack2`.

## Complexity
- **Time Complexity:** O(1) for all operations.
- **Space Complexity:** O(N).

## Code
```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
```
