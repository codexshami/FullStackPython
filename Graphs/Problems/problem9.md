# Problem 9: The Course Scheduler (Course Schedule)

## Problem Statement
There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [a, b]` indicates that you must take course `b` first if you want to take course `a`. Return `true` if you can finish all courses, otherwise return `false`.

## Input Format
- An integer `numCourses`.
- A list of pairs `prerequisites`.

## Constraints
- 1 <= numCourses <= 2000

## Example
**Input:** numCourses = 2, prerequisites = [[1,0]]  
**Output:** True  

**Input:** numCourses = 2, prerequisites = [[1,0],[0,1]]  
**Output:** False (cycle exists)
