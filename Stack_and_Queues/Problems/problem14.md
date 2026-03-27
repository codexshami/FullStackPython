# Problem 14: Processing Throttle

## Problem Statement
Given a characters array `tasks`, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.
However, there is a non-negative integer `n` that represents the cooldown period between two same tasks (the same letter), that is, there must be at least `n` units of time between any two same tasks.
Return the least number of units of time that the CPU will take to finish all the given tasks.

## Input Format
- An array of characters `tasks`.
- An integer `n`.

## Example
**Input:** tasks = ["A","A","A","B","B","B"], n = 2  
**Output:** 8  
**Explanation:** A -> B -> idle -> A -> B -> idle -> A -> B
