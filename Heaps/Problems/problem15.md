# Problem 15: Venture Capital (IPO)

## Problem Statement
Suppose LeetCode will start its IPO soon. To get a good price, LeetCode wants to finish some projects to increase its capital. You are given `n` projects where the ith project has a profit `profits[i]` and a minimum capital `capital[i]` needed to start it.
Initially, you have `w` capital. When you finish a project, you will obtain its profit and your total capital will be increased. You can finish at most `k` distinct projects. Pick a list of at most `k` projects that maximizes your final capital.

## Input Format
- An integer `k`.
- An initial capital `w`.
- An array `profits`.
- An array `capital`.

## Example
**Input:** k = 2, w = 0, profits = [1, 2, 3], capital = [0, 1, 1]  
**Output:** 4  
**Explanation:** Finish project 0 (capital 0) to get profit 1. Total capital becomes 1. Then finish either project 1 or 2 (capital 1) to get profit 3. Total capital becomes 4.
