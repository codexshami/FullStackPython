# Problem 8: The Edit Distance (Edit Distance / Levenshtein Distance)

## Problem Statement
Given two strings `word1` and `word2`, return the minimum number of operations required to convert `word1` to `word2`. You have three operations permitted: Insert a character, Delete a character, Replace a character.

## Input Format
- Two strings `word1` and `word2`.

## Constraints
- 0 <= word1.length, word2.length <= 500

## Example
**Input:** word1 = "horse", word2 = "ros"  
**Output:** 3  
**Explanation:** horse → rorse (replace 'h' with 'r') → rose (remove 'r') → ros (remove 'e').
