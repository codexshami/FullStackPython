# Problem 3: Homogenous Transformation (Longest Repeating Character Replacement)

## Problem Statement
You are given a string `s` and an integer `k`. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most `k` times.
Return the length of the longest substring containing the same letter you can get after performing the above operations.

## Input Format
- A string `s`.
- An integer `k`.

## Example
**Input:** s = "AABABBA", k = 1  
**Output:** 4
**Explanation:** Replace the one 'A' in the middle with 'B' and form "AABBBBA". The substring "BBBB" has the longest repeating character, which is 4.
