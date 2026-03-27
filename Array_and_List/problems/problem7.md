# Problem 7: Targeted Segment Sum

## Problem Statement
Given an unsorted array of non-negative integers `nums` and a non-negative integer `target`, find a contiguous subarray that adds up to the given `target`. Return the starting and ending indices (0-indexed). If no such subarray exists, return `[-1, -1]`.

## Input Format
- An array of integers `nums`.
- An integer `target`.

## Output Format
- A list of two integers representing the indices.

## Constraints
- 1 <= nums.length <= 10^5
- 0 <= nums[i] <= 10^4
- 0 <= target <= 10^9

## Example
**Input:** nums = [1, 4, 20, 3, 10, 5], target = 33  
**Output:** [2, 4]  
**Explanation:** 20 + 3 + 10 = 33.
