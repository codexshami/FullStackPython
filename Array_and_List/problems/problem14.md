# Problem 14: Liquid Capture Potential

## Problem Statement
You are given an integer array `height` where `height[i]` represents the height of a vertical line. Find two lines that together with the x-axis form a container, such that the container contains the most water. Return the maximum amount of water a container can store.

## Input Format
- An array of integers `height`.

## Output Format
- An integer representing the maximum volume.

## Constraints
- 2 <= height.length <= 10^5
- 0 <= height[i] <= 10^4

## Example
**Input:** height = [1, 8, 6, 2, 5, 4, 8, 3, 7]  
**Output:** 49  
**Explanation:** The lines with heights 8 and 7 are at indices 1 and 8. The distance between them is 7. The volume is min(8, 7) * 7 = 49.
