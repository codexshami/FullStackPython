# Problem 13: Maximal Greedy Partitioning (Partition Labels)

## Problem Statement
You are given a string `s`. We want to partition the string into as many parts as possible so that each letter appears in at most one part.
Return a list of integers representing the size of these parts.

## Input Format
- A string `s`.

## Example
**Input:** s = "ababcbacadefegdehijhklij"  
**Output:** [9, 7, 8]  
**Explanation:** The partition is "ababcbaca", "defegde", "hijhklij".
Each letter appears in at most one part.
"ababcbaca" contains 'a', 'b', 'c'. None of these appear in other parts.
