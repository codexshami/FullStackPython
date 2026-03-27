# Problem 18: Algebraic Reconstitution

## Problem Statement
You are given an array `target` of `n` integers. From a starting array `arr` consisting of `n` 1s, you may perform the following procedure:
- Let `x` be the sum of all elements currently in your array.
- Choose index `i` such that `0 <= i < n` and set the value of `arr` at index `i` to `x`.
- You may repeat this procedure any number of times.
Return `True` if it is possible to construct the target array from `arr`, otherwise, return `False`.

## Input Format
- An array of integers `target`.

## Example
**Input:** target = [9, 3, 5]  
**Output:** True  
**Explanation:** [1, 1, 1] sum=3 -> [3, 1, 1] sum=5 -> [3, 5, 1] sum=9 -> [9, 5, 3] (permutation).
