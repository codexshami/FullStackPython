# Problem 16: Sequential Byte Compression (String Compression)

## Problem Statement
Given an array of characters `chars`, compress it using the following algorithm:
Begin with an empty string `s`. For each group of consecutive repeating characters in `chars`:
- If the group's length is 1, append the character to `s`.
- Otherwise, append the character followed by the group's length.
The compressed string `s` should not be returned separately, but instead, be stored in the input character array `chars`. Note that group lengths that are 10 or longer will be split into multiple characters in `chars`.
After you are done modifying the input array, return the new length of the array.

## Input Format
- An array of characters `chars`.

## Example
**Input:** chars = ["a", "a", "b", "b", "c", "c", "c"]  
**Output:** 6, chars = ["a", "2", "b", "2", "c", "3"]
