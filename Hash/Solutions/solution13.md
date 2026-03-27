# Solution 13: Temporally Evicted Memory (LRU Cache)

## Approach Explanation
An LRU Cache requires O(1) time for both `get` and `put`. This is achieved using a Hash Map combined with a Doubly Linked List. The Map provides O(1) lookup, while the List tracks the order of usage.

## Step-by-Step Logic
1. `__init__`: Create a dummy `head` and `tail` for the DLL. Initialize `self.cache` as a map.
2. `_remove(node)`: Remove a node from its current position in the DLL.
3. `_add(node)`: Add a node right before the `tail` (most recent).
4. `get(key)`:
   - If key in cache, remove node from DLL, add it to tail, and return value.
   - Else return -1.
5. `put(key, value)`:
   - If key in cache, remove existing node.
   - Create new node and add to tail. Update cache map.
   - If size > capacity, remove node from head (least recent). Delete from cache map.

## Complexity
- **Time Complexity:** O(1) for both operations.
- **Space Complexity:** O(Capacity).

## Code
```python
class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # map key to node
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
```
