# Problem 6: Perpetual Ranker

## Problem Statement
Design a class `KthLargest` to find the `kth` largest element in a stream. The `kth` largest element is the `kth` largest element in the sorted order, not the `kth` distinct element.
Implement `KthLargest` class:
- `KthLargest(int k, int[] nums)` Initializes the object with the integer `k` and the stream of integers `nums`.
- `int add(int val)` Appends the integer `val` to the stream and returns the element representing the `kth` largest element in the stream.

## Input Format
- Method calls.

## Example
**Input:** ["KthLargest", "add", "add", "add"] [[3, [4, 5, 8, 2]], [3], [5], [10]]  
**Output:** [null, 4, 5, 5]
