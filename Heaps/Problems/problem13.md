# Problem 13: Minimal Domain Covering

## Problem Statement
You have `k` lists of sorted integers in non-decreasing order. Find the smallest range that includes at least one number from each of the `k` lists.
A range `[a, b]` is smaller than range `[c, d]` if `b - a < d - c`, or `a < c` if `b - a == d - c`.

## Input Format
- A 2D array of sorted integers `nums`.

## Example
**Input:** nums = [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]  
**Output:** [20, 24]  
**Explanation:** List 1: 24, List 2: 20, List 3: 22. Range [20, 24] contains one number from each list.
