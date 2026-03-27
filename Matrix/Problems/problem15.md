# Problem 15: Chromatic Saturation (Flood Fill)

## Problem Statement
An image is represented by an `m x n` integer grid `image` where `image[i][j]` represents the pixel value.
You are also given three integers `sr`, `sc`, and `color`. You should perform a flood fill on the image starting from the pixel `image[sr][sc]`.
To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with `color`.

## Input Format
- A 2D integer matrix `image`.
- Starting row `sr` and column `sc`.
- New `color`.

## Example
**Input:** image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]], sr = 1, sc = 1, color = 2  
**Output:** [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
