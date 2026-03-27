# Problem 4: Targeted Extraction

## Problem Statement
Given the `head` of a linked list, remove the `n`-th node from the end of the list and return its head.

## Input Format
- The `head` of a linked list.
- An integer `n`.

## Output Format
- The head of the modified linked list.

## Constraints
- The number of nodes in the list is `sz`.
- 1 <= sz <= 30
- 0 <= Node.val <= 100
- 1 <= n <= sz

## Example
**Input:** head = [1, 2, 3, 4, 5], n = 2  
**Output:** [1, 2, 3, 5]  
**Explanation:** The second node from the end is 4, which is removed.
