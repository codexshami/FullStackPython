# Problem 9: Zero-Sum Game Theory (Predict the Winner)

## Problem Statement
You are given an integer array `nums`. Two players are playing a game with this array: player 1 and player 2.
Player 1 and player 2 take turns, with player 1 starting first. Both players start with a score of 0. At each turn, the player takes one of the numbers from either end of the array (i.e., `nums[0]` or `nums[nums.length - 1]`), which reduces the size of the array by 1. The player adds the chosen number to their score. The game ends when there are no more elements in the array.
Return true if Player 1 can win the game. If the scores of both players are equal, then player 1 is still the winner, and you should also return true. You may assume that both players are playing optimally.

## Input Format
- An array of integers `nums`.

## Example
**Input:** nums = [1, 5, 2]  
**Output:** False  
**Explanation:** Player 1 picks 1 (from end) or 2 (from end). In both cases, player 2 gets 5, leading to player 1 losing.
# Optimal play means maximizing own score and minimizing opponent score.
# Score diff = MyPick - opponent_max_score_diff.
