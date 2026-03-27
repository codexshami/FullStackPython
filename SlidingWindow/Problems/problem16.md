# Problem 16: Sequential Inclusion Span (Minimum Window Subsequence)

## Problem Statement
Given strings `s1` and `s2`, return the minimum contiguous substring of `s1` such that `s2` is a subsequence of the substring.
If there is no such window, return the empty string "". If there are multiple such windows of the same length, return the one with the smallest starting index.

## Input Format
- Two strings `s1` and `s2`.

## Example
**Input:** s1 = "abcdebdde", s2 = "bde"  
**Output:** "bcde"  
**Explanation:** "bcde" is the minimum window that contains "bde" as a subsequence.
# Subsequence means order must be preserved.
