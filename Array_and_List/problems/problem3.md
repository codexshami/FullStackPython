# Problem 3: Cyclical Motion

## Problem Statement
Given an integer array `nums`, rotate the array to the right by `k` steps, where `k` is non-negative.

## Input Format
- An array of integers `nums`.
- An integer `k`.

## Output Format
- The modified array `nums` (or the result after rotation).

## Constraints
- 1 <= nums.length <= 10^5
- -2^31 <= nums[i] <= 2^31 - 1
- 0 <= k <= 10^5

## Example
**Input:** nums = [1, 2, 3, 4, 5, 6, 7], k = 3  
**Output:** [5, 6, 7, 1, 2, 3, 4]  
**Explanation:** 
- rotate 1 steps to the right: [7, 1, 2, 3, 4, 5, 6]
- rotate 2 steps to the right: [6, 7, 1, 2, 3, 4, 5]
- rotate 3 steps to the right: [5, 6, 7, 1, 2, 3, 4]
