# Problem 12: Morphological Reshaping (Matrix Reshape)

## Problem Statement
In MATLAB, there is a handy function called `reshape` which can reshape an `m x n` matrix into a new one with a different size `r x c` keeping its original data.
If the `reshape` operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

## Input Format
- A 2D integer matrix `mat`.
- An integer `r` (new row count).
- An integer `c` (new column count).

## Example
**Input:** mat = [[1, 2], [3, 4]], r = 1, c = 4  
**Output:** [[1, 2, 3, 4]]
