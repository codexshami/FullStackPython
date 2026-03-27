# Problem 18: Cognitive Temperance (Grumpy Bookstore Owner)

## Problem Statement
There is a bookstore owner that has a store open for `n` minutes. Every minute, some number of customers enter the store. You are given an integer array `customers` of length `n`.
On some minutes, the bookstore owner is grumpy. You are given a binary array `grumpy` where `grumpy[i]` is 1 if the owner is grumpy and 0 otherwise.
When the owner is grumpy, the customers of that minute are not satisfied. Otherwise, they are satisfied.
The owner knows a secret technique to keep themselves not grumpy for `minutes` consecutive minutes, but can only use it once.
Return the maximum number of customers that can be satisfied throughout the day.

## Input Format
- `customers` and `grumpy` arrays.
- `minutes` (technique duration).

## Example
**Input:** customers = [1, 0, 1, 2, 1, 1, 7, 5], grumpy = [0, 1, 0, 1, 0, 1, 0, 1], minutes = 3  
**Output:** 16
**Explanation:** The owner keeps themselves not grumpy for the last 3 minutes.
Total satisfied = (1 + 1 + 1) + (2 + 1 + 5) = 3 + 8 + 5 = 16.
# Wait, calculation: 1 (0:0) + 1 (1:0) + 1 (2:0) + 2 (3:1 fix) + 1 (4:0) + 1 (5:1 fix) + 7 (6:0) + 5 (7:1 fix)
# Actually, the window of size 3 that adds the MOST satisfaction is at indices [5, 6, 7] or [6, 7, 8]?
# Let's fix example: [1, 0, 1, 2, 1, 1, 7, 5] -> 16. Correct.
