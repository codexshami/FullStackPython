# Solution 4: LIFO Simulation

## Approach Explanation
We can implement this using a single queue. When pushing an element, we add it to the queue and then rotate the queue (pop and re-append) `n-1` times so that the newest element is at the front.

## Step-by-Step Logic
1. `push(x)`:
   - Add `x` to the queue.
   - For `size - 1` times, dequeue the front element and enqueue it again.
2. `pop()`: Dequeue from the queue.
3. `top()`: Peek at the front of the queue.
4. `empty()`: Check if queue is empty.

## Complexity
- **Time Complexity:** 
  - Push: O(N)
  - Pop: O(1)
- **Space Complexity:** O(N).

## Code
```python
from collections import deque

class MyStack:
    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return not self.queue
```
