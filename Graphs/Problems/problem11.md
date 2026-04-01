# Problem 11: The Flood Fill (Flood Fill Algorithm)

## Problem Statement
An image is represented by an `m x n` integer grid `image` where `image[i][j]` represents the pixel value. Given three integers `sr`, `sc`, and `color`, perform a flood fill on the image starting from pixel `(sr, sc)`. Change all connected pixels of the same color to `color`.

## Input Format
- A 2D grid `image`.
- Integers `sr`, `sc` (starting position).
- Integer `color` (new color).

## Example
**Input:** image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2  
**Output:** [[2,2,2],[2,2,0],[2,0,1]]
