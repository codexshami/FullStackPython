# Problem 14: Resource Balancing Strategy (Bag of Tokens)

## Problem Statement
You have an initial power `P`, an initial score of 0, and a bag of `tokens` where `tokens[i]` is the value of the `i-th` token.
Your goal is to maximize your total score by potentially playing each token in one of two ways:
1. If your current power is at least `tokens[i]`, you may play the `i-th` token face up, losing `tokens[i]` power and gaining 1 score.
2. If your current score is at least 1, you may play the `i-th` token face down, gaining `tokens[i]` power and losing 1 score.
Each token can be played at most once and in any order. You do not have to play all the tokens.
Return the largest possible score you can achieve after playing any number of tokens.

## Input Format
- An array of integers `tokens`.
- An integer `power`.

## Example
**Input:** tokens = [100, 200, 300, 400], power = 200  
**Output:** 2
