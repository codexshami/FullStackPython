# Problem 10: Structural Logic Emulation (Design HashMap)

## Problem Statement
Design a HashMap without using any built-in hash table libraries.
Implement the `MyHashMap` class:
- `MyHashMap()` initializes the object.
- `void put(int key, int value)` inserts a `(key, value)` pair into the HashMap. If the key already exists, update the corresponding value.
- `int get(int key)` returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
- `void remove(key)` removes the key and its corresponding value if the map contains the mapping for the key.

## Input Format
- Method calls.

## Example
**Input:** ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"] [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]  
**Output:** [null, null, null, 1, -1, null, 1, null, -1]
