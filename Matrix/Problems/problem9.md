# Problem 9: Efficient Dot Product (Sparse Matrix Multiplication)

## Problem Statement
Given two sparse matrices `mat1` of size `m x k` and `mat2` of size `k x n`, return the result of `mat1 * mat2`.
You may assume that the intermediate values of the product fit in a 32-bit integer.

## Input Format
- Two 2D integer matrices.

## Example
**Input:** mat1 = [[1, 0, 0], [-1, 0, 3]], mat2 = [[7, 0, 0], [0, 0, 0], [0, 0, 1]]  
**Output:** [[7, 0, 0], [-7, 0, 3]]
