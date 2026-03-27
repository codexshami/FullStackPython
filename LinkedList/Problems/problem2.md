# Problem 2: Circular Entrapment

## Problem Statement
Given `head`, the head of a linked list, determine if the linked list has a cycle in it. There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer.

## Input Format
- The `head` of a linked list.

## Output Format
- Boolean: `True` if there is a cycle, `False` otherwise.

## Constraints
- The number of nodes in the list is in the range [0, 10^4].
- -10^5 <= Node.val <= 10^5

## Example
**Input:** head = [3, 2, 0, -4], pos = 1 (tail connects to node index 1)  
**Output:** True  
**Explanation:** There is a cycle in the linked list, where the tail connects to the 1st node.
