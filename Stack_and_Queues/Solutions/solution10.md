# Solution 10: Seamless Ring Buffer

## Approach Explanation
We use an array of fixed size and two pointers, `head` and `count` (or `head` and `tail`). Using `count` simplifies the logic for checking if the queue is full or empty.

## Step-by-Step Logic
1. Initialize an array of size `k`, `head_index = 0`, and `current_size = 0`.
2. `enQueue(val)`: If `current_size == k`, return `False`. Calculate `tail_index = (head_index + current_size) % k`, place value, and increment `current_size`.
3. `deQueue()`: If `current_size == 0`, return `False`. Move `head_index = (head_index + 1) % k` and decrement `current_size`.
4. `Front()`: Return `queue[head_index]` if not empty.
5. `Rear()`: Return `queue[(head_index + current_size - 1) % k]` if not empty.

## Complexity
- **Time Complexity:** O(1) for all operations.
- **Space Complexity:** O(k), where k is the size of the queue.

## Code
```python
class MyCircularQueue:
    def __init__(self, k: int):
        self.queue = [0] * k
        self.k = k
        self.head = 0
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        # Calculate tail index relative to head
        idx = (self.head + self.size) % self.k
        self.queue[idx] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.head = (self.head + 1) % self.k
        self.size -= 1
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.queue[self.head]

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        idx = (self.head + self.size - 1) % self.k
        return self.queue[idx]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k
```
