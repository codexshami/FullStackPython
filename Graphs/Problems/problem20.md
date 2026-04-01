# Problem 20: The Network Delay (Network Delay Time)

## Problem Statement
You are given a network of `n` nodes, labeled from `1` to `n`. You are also given `times`, a list of travel times as directed edges `times[i] = (u, v, w)` where `u` is the source, `v` is the target, and `w` is the time. Send a signal from a given node `k`. Return the minimum time it takes for all `n` nodes to receive the signal. If it's impossible, return -1.

## Input Format
- A list of edges `times`.
- Integers `n` and `k`.

## Constraints
- 1 <= k <= n <= 100

## Example
**Input:** times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2  
**Output:** 2
