# Problem 12: Range-Bounded Count (Number of Subarrays with Bounded Maximum)

## Problem Statement
Given an integer array `nums` and two integers `left` and `right`, return the number of contiguous non-empty subarrays such that the value of the maximum array element in that subarray is in the range `[left, right]`.

## Input Format
- An array of integers `nums`.
- Integers `left` and `right`.

## Example
**Input:** nums = [2, 1, 4, 3], left = 2, right = 3  
**Output:** 3  
**Explanation:** There are three subarrays that meet the requirements: [2], [2, 1], [3].
