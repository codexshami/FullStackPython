# Problem 17: Allocation Capacity (Meeting Rooms II)

## Problem Statement
Given an array of meeting time intervals `intervals` where `intervals[i] = [start_i, end_i]`, return the minimum number of conference rooms required.

## Input Format
- A 2D array of intervals.

## Example
**Input:** intervals = [[0, 30], [5, 10], [15, 20]]  
**Output:** 2
**Explanation:** 
- Meeting 1: [0, 30] needs Room 1.
- Meeting 2: [5, 10] starts when Room 1 is busy, needs Room 2.
- Meeting 3: [15, 20] starts when Room 1 is busy, but Room 2 is free. Use Room 2.
- Total 2 rooms.
