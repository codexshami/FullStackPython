# Problem 15: Sequence Verification

## Problem Statement
Given two integer arrays `pushed` and `popped` each with distinct values, return `True` if this could have been the result of a sequence of push and pop operations on an initially empty stack, or `False` otherwise.

## Input Format
- Two integer arrays `pushed` and `popped`.

## Example
**Input:** pushed = [1, 2, 3, 4, 5], popped = [4, 5, 3, 2, 1]  
**Output:** True  
**Explanation:** push(1), push(2), push(3), push(4), pop() -> 4, push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1.
