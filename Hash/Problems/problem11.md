# Problem 11: Binary Set Logic (Design HashSet)

## Problem Statement
Design a HashSet without using any built-in hash table libraries.
Implement the `MyHashSet` class:
- `MyHashSet()` initializes the object.
- `void add(key)` inserts the value `key` into the HashSet.
- `bool contains(key)` returns whether the value `key` exists in the HashSet or not.
- `void remove(key)` removes the value `key` in the HashSet. If `key` does not exist in the HashSet, do nothing.

## Input Format
- Method calls.

## Example
**Input:** ["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"] [[], [1], [2], [1], [3], [2], [2], [2], [2]]  
**Output:** [null, null, null, true, false, null, true, null, false]
