# Problem 17: Dissimilarity Quantile (Find K-th Smallest Pair Distance)

## Problem Statement
The distance of a pair of integers `a` and `b` is defined as the absolute difference between `a` and `b`.
Given an integer array `nums` and an integer `k`, return the `k-th` smallest distance among all the pairs `nums[i]` and `nums[j]` where `0 <= i < j < nums.length`.

## Input Format
- An array of integers `nums`.
- An integer `k`.

## Example
**Input:** nums = [1, 3, 1], k = 1  
**Output:** 0
**Explanation:** Possible pairs are (1, 3), (1, 1), (3, 1). Absolute differences are 2, 0, 2. The 1st smallest distance is 0.
