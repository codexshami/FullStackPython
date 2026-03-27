# Problem 10: Task Orchestration

## Problem Statement
You are given `n` tasks, where `tasks[i] = [enqueueTime, processingTime]`. You have a single-threaded CPU that can process at most one task at a time.
1. If the CPU is idle and there are available tasks, the CPU will choose the one with the shortest processing time. If there is a tie, it chooses the task with the smallest index.
2. Once the CPU starts a task, it will finish the entire task without stopping.
Return the order in which the CPU will process the tasks.

## Input Format
- A 2D array `tasks`.

## Example
**Input:** tasks = [[1, 2], [2, 4], [3, 2], [4, 1]]  
**Output:** [0, 2, 3, 1]
