# Problem 15: Optimal Vessel Occupancy (Boats to Save People)

## Problem Statement
You are given an array `people` where `people[i]` is the weight of the `i-th` person, and an infinite number of boats where each boat can carry a maximum weight of `limit`. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most `limit`.
Return the minimum number of boats to carry every given person.

## Input Format
- An array of integers `people`.
- An integer `limit`.

## Example
**Input:** people = [3, 2, 2, 1], limit = 3  
**Output:** 3  
**Explanation:** 3 boats (1, 2), (2), (3).
