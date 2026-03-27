# Problem 11: Canonical Path Canonicalizer (Simplify Path)

## Problem Statement
Given a string `path`, which is an absolute path (starting with a slash '/') to a file or directory in a Unix-style file system, convert it to the simplified canonical path.
In a Unix-style file system:
- A period '.' refers to the current directory.
- A double period '..' refers to the directory up a level.
- Multiple consecutive slashes (e.g., '//') are treated as a single slash '/'.

## Input Format
- A string `path`.

## Example
**Input:** path = "/home//foo/"  
**Output:** "/home/foo"
**Input:** path = "/../"  
**Output:** "/"
