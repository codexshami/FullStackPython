# Problem 7: Seasonal Transition

## Problem Statement
Given an array of integers `temperatures` representing the daily temperatures, return an array `answer` such that `answer[i]` is the number of days you have to wait after the i-th day to get a warmer temperature. If there is no future day for which this is possible, keep `answer[i] == 0` instead.

## Input Format
- An array of integers `temperatures`.

## Example
**Input:** temperatures = [73, 74, 75, 71, 69, 72, 76, 73]  
**Output:** [1, 1, 4, 2, 1, 1, 0, 0]
