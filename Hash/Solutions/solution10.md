# Solution 10: Structural Logic Emulation (Design HashMap)

## Approach Explanation
We use separate chaining to handle collisions. We create a list of "buckets", where each bucket is a linked list (or simple list) of `(key, value)` pairs.

## Step-by-Step Logic
1. `__init__`: Create `self.size = 1000` and `self.buckets = [[] for _ in range(self.size)]`.
2. `_hash(key)`: Return `key % self.size`.
3. `put(key, value)`:
   - Find bucket. Iterate through pairs. If key exists, update value and return.
   - If not found, append `[key, value]`.
4. `get(key)`:
   - Find bucket. Iterate. If key found, return value.
   - Else return -1.
5. `remove(key)`:
   - Find bucket. Iterate. If key exists, `pop` or `remove` from bucket.

## Complexity
- **Time Complexity:** O(N / K) average, where K is size (1000).
- **Space Complexity:** O(N + K).

## Code
```python
class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        idx = self._hash(key)
        for i, (k, v) in enumerate(self.buckets[idx]):
            if k == key:
                self.buckets[idx][i] = (key, value)
                return
        self.buckets[idx].append((key, value))

    def get(self, key: int) -> int:
        idx = self._hash(key)
        for k, v in self.buckets[idx]:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        idx = self._hash(key)
        for i, (k, v) in enumerate(self.buckets[idx]):
            if k == key:
                self.buckets[idx].pop(i)
                return
```
