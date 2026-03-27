# Problem 10: Peak Mountaineer

## Problem Statement
A peak element is an element that is strictly greater than its neighbors. Given an integer array `nums`, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks. You may imagine that `nums[-1] = nums[n] = -∞`. You must write an algorithm that runs in O(log N) time.

## Input Format
- An array of integers `nums`.

## Output Format
- An integer representing the index of any peak element.

## Constraints
- 1 <= nums.length <= 1000
- -2^31 <= nums[i] <= 2^31 - 1
- `nums[i] != nums[i + 1]` for all valid `i`.

## Example
**Input:** nums = [1, 2, 1, 3, 5, 6, 4]  
**Output:** 5  
**Explanation:** Your function can return either index 1 where the peak element is 2, or index 5 where the peak element is 6.
