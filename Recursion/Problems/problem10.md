# Problem 10: Eliminative Circular Logic (Josephus Problem)

## Problem Statement
There are `n` people standing in a circle. They are numbered from 1 to `n` in clockwise order.
Starting from the first person, we go clockwise and skip `k-1` people, and the `k-th` person is eliminated. The process continues until only one person remains.
Return the index of the last person remaining.

## Input Format
- Two integers `n` and `k`.

## Example
**Input:** n = 5, k = 2  
**Output:** 3  
**Explanation:** 
1. 2 is eliminated. (1, 3, 4, 5) remains.
2. 4 is eliminated. (1, 3, 5) remains.
3. 1 is eliminated. (3, 5) remains.
4. 5 is eliminated. 3 remains.
# Josephus formula: J(n, k) = (J(n-1, k) + k) % n.
