# Problem 11: Dimensional Accordion

## Problem Statement
You are given a doubly linked list, which contains nodes that have a next pointer, a previous pointer, and an additional child pointer. This child pointer may or may not point to a separate doubly linked list, also containing these special nodes. Flatten the list so that all the nodes appear in a single-level, doubly linked list.

## Input Format
- The `head` of a multilevel doubly linked list.

## Output Format
- The `head` of the flattened doubly linked list.

## Example
**Input:** head = [1, 2, 3, 4, 5, 6, null, null, null, 7, 8, 9, 10, null, null, 11, 12]  
**Output:** [1, 2, 3, 7, 8, 11, 12, 9, 10, 4, 5, 6]
