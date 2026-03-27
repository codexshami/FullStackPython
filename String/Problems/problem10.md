# Problem 10: Recursive Expansion (Decode String)

## Problem Statement
Given an encoded string, return its decoded string.
The encoding rule is: `k[encoded_string]`, where the `encoded_string` inside the square brackets is being repeated exactly `k` times. Note that `k` is guaranteed to be a positive integer.
You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc.

## Input Format
- An encoded string `s`.

## Example
**Input:** s = "3[a]2[bc]"  
**Output:** "aaabcbc"
**Input:** s = "3[a2[c]]"  
**Output:** "accaccacc"
