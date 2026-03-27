# Problem 8: Merging Overlaps

## Problem Statement
Given an array of `intervals` where `intervals[i] = [start_i, end_i]`, merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

## Input Format
- A 2D array representing intervals.

## Output Format
- A 2D array representing merged intervals.

## Constraints
- 1 <= intervals.length <= 10^4
- intervals[i].length == 2
- 0 <= start_i <= end_i <= 10^4

## Example
**Input:** intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]  
**Output:** [[1, 6], [8, 10], [15, 18]]  
**Explanation:** [1, 3] and [2, 6] overlap, so they are merged into [1, 6].
