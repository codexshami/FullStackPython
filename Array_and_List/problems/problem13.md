# Problem 13: Triple Sum Discovery

## Problem Statement
Given an integer array `nums`, return all the unique triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`. The solution set must not contain duplicate triplets.

## Input Format
- An array of integers `nums`.

## Output Format
- A list of lists representing the triplets.

## Constraints
- 3 <= nums.length <= 3000
- -10^5 <= nums[i] <= 10^5

## Example
**Input:** nums = [-1, 0, 1, 2, -1, -4]  
**Output:** [[-1, -1, 2], [-1, 0, 1]]  
**Explanation:** 
- nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
- nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
- Result should not contain duplicate triplets like [-1, 0, 1] twice.
