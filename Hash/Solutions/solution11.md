# Solution 11: Binary Set Logic (Design HashSet)

## Approach Explanation
Like the HashMap, we use separate chaining with a prime number of buckets to minimize collisions.

## Step-by-Step Logic
1. `__init__`: `self.size = 769`, `self.buckets = [[] for _ in range(self.size)]`.
2. `_hash(key)`: `key % self.size`.
3. `add(key)`:
   - Check if `key` is in `self.buckets[idx]`.
   - If not, append it.
4. `contains(key)`:
   - Return `True` if `key` is in `self.buckets[idx]`.
5. `remove(key)`:
   - If `key` is in `self.buckets[idx]`, `remove` it.

## Complexity
- **Time Complexity:** O(N / K).
- **Space Complexity:** O(N + K).

## Code
```python
class MyHashSet:
    def __init__(self):
        self.size = 769
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key):
        return key % self.size

    def add(self, key: int) -> None:
        idx = self._hash(key)
        if key not in self.buckets[idx]:
            self.buckets[idx].append(key)

    def contains(self, key: int) -> bool:
        idx = self._hash(key)
        return key in self.buckets[idx]

    def remove(self, key: int) -> None:
        idx = self._hash(key)
        if key in self.buckets[idx]:
            self.buckets[idx].remove(key)
```
