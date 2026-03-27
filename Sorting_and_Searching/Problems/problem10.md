# Problem 10: Partition Optimization

## Problem Statement
Given an integer array `nums` and an integer `k`, split `nums` into `k` non-empty subarrays such that the largest sum of any subarray is minimized. Return the minimized largest sum of the split.
A subarray is a contiguous part of the array.

## Input Format
- An array `nums`.
- An integer `k`.

## Example
**Input:** nums = [7, 2, 5, 10, 8], k = 2  
**Output:** 18  
**Explanation:** Split into [7, 2, 5] and [10, 8]. Max sum is max(14, 18) = 18.
- Other splits like [7, 2] and [5, 10, 8] would have max sum 23.
