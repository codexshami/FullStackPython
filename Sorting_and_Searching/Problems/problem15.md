# Problem 15: Adaptive Insertion (Insert Interval)

## Problem Statement
You are given an array of non-overlapping intervals `intervals` where `intervals[i] = [start_i, end_i]` sorted in ascending order by `start_i`. You are also given an interval `newInterval = [start, end]` that represents the start and end of another interval.
Insert `newInterval` into `intervals` such that `intervals` is still sorted in ascending order by `start_i` and `intervals` still does not have any overlapping intervals (merge overlapping intervals if necessary).

## Input Format
- A sorted 2D array of intervals.
- A new interval.

## Example
**Input:** intervals = [[1, 3], [6, 9]], newInterval = [2, 5]  
**Output:** [[1, 5], [6, 9]]
