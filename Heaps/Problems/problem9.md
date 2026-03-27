# Problem 9: Architectural Ascent

## Problem Statement
You are given an integer array `heights` representing the heights of buildings, some `bricks`, and some `ladders`. You start your journey from building 0 and move to building `i+1`.
- If the current building's height is greater than or equal to the next building's height, you do not need a ladder or bricks.
- If the next building's height is greater than the current building's height, you can either use one ladder or `(h[i+1] - h[i])` bricks.
Return the furthest building index you can reach.

## Input Format
- An array of integers `heights`.
- An integer `bricks`.
- An integer `ladders`.

## Example
**Input:** heights = [4, 2, 7, 6, 9, 14, 12], bricks = 5, ladders = 1  
**Output:** 4
**Explanation:** Use bricks for 2->7 (5 bricks), then use ladder for 6->9.
