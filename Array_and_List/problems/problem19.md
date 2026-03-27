# Problem 19: Minimal Fusion Cost

## Problem Statement
There are `n` piles of stones arranged in a row. The i-th pile has `stones[i]` stones. A move consists of merging exactly `k` consecutive piles into one pile, and the cost of this move is equal to the total number of stones in these `k` piles. Find the minimum cost to merge all piles into one pile. If it is impossible, return -1.

## Input Format
- An array of integers `stones`.
- An integer `k`.

## Output Format
- An integer representing the minimum cost.

## Constraints
- 1 <= stones.length <= 30
- 2 <= k <= 30
- 1 <= stones[i] <= 100

## Example
**Input:** stones = [3, 2, 4, 1], k = 2  
**Output:** 20  
**Explanation:** 
- Merge [3, 2] for cost 5. Result: [5, 4, 1]
- Merge [4, 1] for cost 5. Result: [5, 5]
- Merge [5, 5] for cost 10. Result: [10]
- Total cost = 5 + 5 + 10 = 20.
