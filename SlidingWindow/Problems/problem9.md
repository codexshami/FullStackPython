# Problem 9: Orchard Greedy Strategy (Fruit Into Baskets)

## Problem Statement
You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array `fruits` where `fruits[i]` is the type of fruit the `i-th` tree produces.
You have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
For every tree encountered, you must put one fruit into one of your baskets. If you reach a tree with a fruit type that does not fit in either basket, you must stop.
Return the maximum number of fruits you can collect.

## Input Format
- An array of integers `fruits`.

## Example
**Input:** fruits = [1, 2, 3, 2, 2]  
**Output:** 4  
**Explanation:** We can collect [2, 3, 2, 2].
