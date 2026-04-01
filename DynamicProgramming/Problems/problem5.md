# Problem 5: The Knapsack Challenge (0/1 Knapsack)

## Problem Statement
Given `n` items, each with a weight and a value, determine the maximum total value that can be put in a knapsack of capacity `W`. You cannot break an item — either pick the complete item or don't pick it (0/1 property).

## Input Format
- An integer `W` (knapsack capacity).
- Arrays `weights` and `values` of length `n`.

## Constraints
- 1 <= n <= 100
- 1 <= W <= 1000

## Example
**Input:** W = 50, weights = [10, 20, 30], values = [60, 100, 120]  
**Output:** 220  
**Explanation:** Take items with weights 20 and 30 (values 100 + 120 = 220).
