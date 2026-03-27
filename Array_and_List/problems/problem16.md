# Problem 16: Interleaved Middle Find

## Problem Statement
Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return the median of the two sorted arrays. The overall run time complexity should be O(log(m+n)).

## Input Format
- Two sorted arrays of integers `nums1` and `nums2`.

## Output Format
- A float representing the median value.

## Constraints
- nums1.length == m, nums2.length == n
- 0 <= m, n <= 1000
- 1 <= m + n <= 2000
- -10^6 <= nums1[i], nums2[i] <= 10^6

## Example
**Input:** nums1 = [1, 3], nums2 = [2]  
**Output:** 2.0  
**Explanation:** Merged array = [1, 2, 3], median is 2.0.
