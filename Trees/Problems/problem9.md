# Problem 9: Integrity Audit

## Problem Statement
Given the `root` of a binary tree, determine if it is a valid binary search tree (BST).
A valid BST is defined as follows:
- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

## Input Format
- The `root` of a binary tree.

## Example
**Input:** root = [5, 1, 4, null, null, 3, 6]  
**Output:** False  
**Explanation:** Root is 5, but its right child's left child is 3 (3 < 5).
