# Problem 19: High Frequency Cache (LFU)

## Problem Statement
Design a data structure that follows the constraints of a Least Frequently Used (LFU) cache. Implement the `LFUCache` class:
- `get(key)`: Return the value if key exists, otherwise -1.
- `put(key, value)`: Update value if key exists, otherwise add it. Evict the least frequently used key. If there is a tie, evict the least recently used key.

## Input Format
- Capacity and various method calls.

## Constraints
- 0 <= capacity <= 10^4
- All operations must be O(1).

## Example
**Input:** ["LFUCache", "put", "put", "get", "put"] [[2], [1, 1], [2, 2], [1], [3, 3]]  
**Output:** [null, null, null, 1, null]
