# Problem 8: Logistics Optimization

## Problem Statement
A conveyor belt has packages that must be shipped from one port to another within `days` days.
The ith package on the conveyor belt has a weight of `weights[i]`. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We cannot load more weight than the maximum weight capacity of the ship.
Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within `days` days.

## Input Format
- An array of weights `weights`.
- An integer `days`.

## Example
**Input:** weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], days = 5  
**Output:** 15  
**Explanation:** A ship capacity of 15 is the minimum to ship all packages in 5 days.
- Day 1: 1, 2, 3, 4, 5 (total 15)
- Day 2: 6, 7 (total 13)
- Day 3: 8 (total 8)
- Day 4: 9 (total 9)
- Day 5: 10 (total 10)
