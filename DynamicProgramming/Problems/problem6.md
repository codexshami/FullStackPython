# Problem 6: The Coin Puzzle (Coin Change)

## Problem Statement
You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money. Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return `-1`.

## Input Format
- An array of integers `coins`.
- An integer `amount`.

## Constraints
- 1 <= coins.length <= 12
- 1 <= coins[i] <= 2^31 - 1
- 0 <= amount <= 10^4

## Example
**Input:** coins = [1, 5, 11], amount = 15  
**Output:** 3  
**Explanation:** 15 = 5 + 5 + 5.
