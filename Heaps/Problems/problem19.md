# Problem 19: Logistical Endurance

## Problem Statement
A car travels from a starting position to a `target` destination. The car has an initial amount of `fuel`. Along the way, there are gas `stations` where `stations[i] = [position_i, fuel_i]` indicates that at `position_i` there is a gas station with `fuel_i` amount of fuel.
You want to reach the `target` with the minimum number of refueling stops. If you cannot reach the target, return -1.

## Input Format
- An integer `target`.
- An integer `startFuel`.
- A 2D array `stations`.

## Example
**Input:** target = 100, startFuel = 10, stations = [[10, 60], [20, 30], [30, 30], [60, 40]]  
**Output:** 2
**Explanation:** Start with 10. Reach station at 10. Refuel 60 (total 70). Reach station at 60. Refuel 40 (total 110). Reach 100.
