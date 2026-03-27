# Problem 18: Adaptive Cache (LRU)

## Problem Statement
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache. Implement the `LRUCache` class:
- `get(key)`: Return the value if key exists, otherwise -1.
- `put(key, value)`: Update value if key exists, otherwise add it. If cache is full, evict the least recently used key.

## Input Format
- Capacity and various method calls.

## Output Format
- Results of `get` calls.

## Constraints
- 1 <= capacity <= 3000
- 0 <= key <= 10^4
- 0 <= value <= 10^5

## Example
**Input:** ["LRUCache", "put", "put", "get", "put", "get"] [[2], [1, 1], [2, 2], [1], [3, 3], [2]]  
**Output:** [null, null, null, 1, null, -1]
