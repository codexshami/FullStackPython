# Solution 19: High Frequency Cache (LFU)

## Approach Explanation
We use two hash maps and doubly linked lists. One map stores the key-node mapping, and another map stores `frequency -> DoublyLinkedList`. This allows us to track both frequency and the LRU order within that frequency in O(1).

## Step-by-Step Logic
1. `node_map`: maps `key` to `Node`.
2. `freq_map`: maps `frequency` to a doubly linked list of nodes with that frequency.
3. `min_freq`: tracks the minimum frequency currently in the cache.
4. When a node is accessed: increment its frequency, move it to the new frequency's list, and update `min_freq` if necessary.
5. When adding at capacity: remove from `freq_map[min_freq]` using LRU logic.

## Complexity
- **Time Complexity:** O(1) for all operations.
- **Space Complexity:** O(C), where C is the capacity.

## Code
```python
from collections import defaultdict

class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.freq = 1
        self.prev = self.next = None

class DLinkedList:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next, self.tail.prev = self.tail, self.head
        self.size = 0
    def add(self, node):
        node.next = self.head.next
        node.next.prev = node
        self.head.next = node
        node.prev = self.head
        self.size += 1
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
        return node
    def pop_tail(self):
        return self.remove(self.tail.prev)

class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.node_map = {}
        self.freq_map = defaultdict(DLinkedList)
        self.min_freq = 0

    def _update_freq(self, node):
        f = node.freq
        self.freq_map[f].remove(node)
        if f == self.min_freq and self.freq_map[f].size == 0:
            self.min_freq += 1
        node.freq += 1
        self.freq_map[node.freq].add(node)

    def get(self, key):
        if key not in self.node_map: return -1
        node = self.node_map[key]
        self._update_freq(node)
        return node.val

    def put(self, key, value):
        if self.capacity == 0: return
        if key in self.node_map:
            node = self.node_map[key]
            node.val = value
            self._update_freq(node)
        else:
            if len(self.node_map) >= self.capacity:
                lfu_node = self.freq_map[self.min_freq].pop_tail()
                del self.node_map[lfu_node.key]
            new_node = Node(key, value)
            self.node_map[key] = new_node
            self.freq_map[1].add(new_node)
            self.min_freq = 1
```
