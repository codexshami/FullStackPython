# Problem 7: Minimal Consumption Rate

## Problem Statement
Koko loves to eat bananas. There are `n` piles of bananas, the ith pile has `piles[i]` bananas. The guards have gone and will come back in `h` hours.
Koko can decide her bananas-per-hour eating speed of `k`. Each hour, she chooses some pile of bananas and eats `k` bananas from that pile. If the pile has less than `k` bananas, she eats all of them instead and will not eat any more bananas during this hour.
Koko wants to finish eating all the bananas before the guards return. Return the minimum integer `k` such that she can eat all the bananas within `h` hours.

## Input Format
- An array `piles`.
- An integer `h`.

## Example
**Input:** piles = [3, 6, 7, 11], h = 8  
**Output:** 4
