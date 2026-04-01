# Problem 19: The Unbounded Knapsack (Coin Change II — Number of Ways)

## Problem Statement
You are given an integer array `coins` representing coins of different denominations and an integer `amount`. Return the number of combinations that make up that amount. If that amount cannot be made up, return 0.

## Input Format
- An array of integers `coins`.
- An integer `amount`.

## Constraints
- 1 <= coins.length <= 300
- 1 <= coins[i] <= 5000
- 0 <= amount <= 5000

## Example
**Input:** amount = 5, coins = [1, 2, 5]  
**Output:** 4  
**Explanation:** 5=5, 5=2+2+1, 5=2+1+1+1, 5=1+1+1+1+1.
