# Problem 9: Absolute Path Normalizer

## Problem Statement
Given an absolute path for a Unix-style file system, which begins with a slash `/`, transform it to the simplified canonical path.
Rules:
- `.` refers to current directory.
- `..` refers to parent directory.
- Multiple slashes `//` are treated as a single slash.
- The path must start with `/` and not end with `/`.

## Input Format
- A string `path`.

## Example
**Input:** path = "/home//foo/"  
**Output:** "/home/foo"
