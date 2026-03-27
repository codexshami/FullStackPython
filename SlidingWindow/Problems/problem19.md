# Problem 19: Boundary Selection Strategy (Maximum Points You Can Obtain from Cards)

## Problem Statement
There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array `cardPoints`.
In one step, you can take one card from either the beginning or from the end of the row. You have to take exactly `k` cards.
Your score is the sum of the points of the cards you have taken.
Return the maximum score you can obtain.

## Input Format
- An array of integers `cardPoints`.
- An integer `k`.

## Example
**Input:** cardPoints = [1, 2, 3, 4, 5, 6, 1], k = 3  
**Output:** 12
**Explanation:** Pick the last three cards (sum: 5+6+1=12).
