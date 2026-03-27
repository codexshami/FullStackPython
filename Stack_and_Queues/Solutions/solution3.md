# Solution 3: FIFO Simulation

## Approach Explanation
We use two stacks: `s1` for pushing elements and `s2` for popping/peeking. When `s2` is empty, we transfer all elements from `s1` to `s2`, which reverses their order and achieves FIFO behavior.

## Step-by-Step Logic
1. `push(x)`: Append to `s1`.
2. `pop()`:
   - If `s2` is empty, pop all elements from `s1` and push them to `s2`.
   - Pop from `s2`.
3. `peek()`:
   - If `s2` is empty, transfer from `s1` to `s2`.
   - Return the top of `s2`.
4. `empty()`: Return true if both stacks are empty.

## Complexity
- **Time Complexity:** 
  - Push: O(1)
  - Pop/Peek: Amortized O(1). Each element is moved at most twice.
- **Space Complexity:** O(N).

## Code
```python
class MyQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)

    def _transfer(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())

    def pop(self) -> int:
        self._transfer()
        return self.s2.pop()

    def peek(self) -> int:
        self._transfer()
        return self.s2[-1]

    def empty(self) -> bool:
        return not self.s1 and not self.s2
```
