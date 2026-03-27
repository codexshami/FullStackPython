# Solution 18: Adaptive Cache (LRU)

## Approach Explanation
We use a combination of a Hash Map and a Doubly Linked List. The hash map provides O(1) access to nodes, while the doubly linked list maintains the usage order. We move any accessed or newly added node to the "front" (most recent) and evict from the "back" (least recent).

## Step-by-Step Logic
1. Create a `Node` class with `key`, `val`, `prev`, and `next`.
2. In `LRUCache`, maintain a map `cache` and dummy nodes `head` and `tail`.
3. `get(key)`: If `key` in `cache`, move that node to the head and return value.
4. `put(key, value)`:
   - If `key` in `cache`, update value and move to head.
   - Else:
     - If at capacity, remove `tail.prev`.
     - Add new node at head.
5. All operations run in O(1).

## Complexity
- **Time Complexity:** O(1) for both `get` and `put`.
- **Space Complexity:** O(C), where C is the capacity.

## Code
```python
class Node:
    def __init__(self, key=0, val=0):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.head, self.tail = Node(), Node()
        self.head.next, self.tail.prev = self.tail, self.head

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add(self, node):
        node.next = self.head.next
        node.next.prev = node
        self.head.next = node
        node.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        node = Node(key, value)
        self.cache[key] = node
        self._add(node)
        if len(self.cache) > self.cap:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]
```
