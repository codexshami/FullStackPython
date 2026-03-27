# Problem 12: Railway Station Congestion

## Problem Statement
Given arrival and departure times of all trains that reach a railway station, find the minimum number of platforms required for the railway station so that no train has to wait.

## Input Format
- Two arrays: `arrival` (sorted) and `departure` (unsorted or sorted).

## Output Format
- An integer representing the minimum number of platforms.

## Constraints
- 1 <= arrival.length <= 10^5
- arrival.length == departure.length

## Example
**Input:** arrival = [900, 940, 950, 1100, 1500, 1800], departure = [910, 1200, 1120, 1130, 1900, 2000]  
**Output:** 3  
**Explanation:** 
- At 9:00: Train 1 arrives (Platform count 1)
- At 9:10: Train 1 departs (Platform count 0)
- At 9:40: Train 2 arrives (Platform count 1)
- At 9:50: Train 3 arrives (Platform count 2)
- At 11:00: Train 4 arrives (Platform count 3)
- ...At peak, 3 trains are in the station.
