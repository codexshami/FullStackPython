# Problem 6: Distributed Multiplication

## Problem Statement
Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`. The product is guaranteed to fit in a 32-bit integer. You must solve this in O(N) time and without using the division operator.

## Input Format
- An array of integers `nums`.

## Output Format
- An array of integers `answer`.

## Constraints
- 2 <= nums.length <= 10^5
- -30 <= nums[i] <= 30
- The product is guaranteed to fit in a 32-bit integer.

## Example
**Input:** nums = [1, 2, 3, 4]  
**Output:** [24, 12, 8, 6]  
**Explanation:** 
- answer[0] = 2 * 3 * 4 = 24
- answer[1] = 1 * 3 * 4 = 12
- answer[2] = 1 * 2 * 4 = 8
- answer[3] = 1 * 2 * 3 = 6
