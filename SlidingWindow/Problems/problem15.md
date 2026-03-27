# Problem 15: Cardinality Constraint (Subarrays with K Different Integers)

## Problem Statement
Given an integer array `nums` and an integer `k`, return the number of good subarrays of `nums`.
A good subarray is an array where the number of different integers in that array is exactly `k`.

## Input Format
- An array of integers `nums`.
- An integer `k`.

## Example
**Input:** nums = [1, 2, 1, 2, 3], k = 2  
**Output:** 7  
**Explanation:** Subarrays formed with exactly 2 different integers: [1, 2], [2, 1], [1, 2], [2, 3], [1, 2, 1], [2, 1, 2], [1, 2, 1, 2].
# Wait, let me double check the example result 7.
# [1,2], [2,1], [1,2], [2,3] -> 4
# [1,2,1], [2,1,2], [1,2,1,2] -> 3
# Total = 7. Correct.
