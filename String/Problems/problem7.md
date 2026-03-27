# Problem 7: Lexical Integer Extraction (atoi)

## Problem Statement
Implement the `myAtoi(string s)` function, which converts a string to a 32-bit signed integer.
Key rules:
1. Whitespace: Ignore leading whitespace.
2. Signedness: Determine if the result is positive or negative based on '-' or '+'.
3. Conversion: Read characters until a non-digit character is encountered.
4. Rounding: If the integer is out of the 32-bit signed integer range, clamp it to INT_MIN or INT_MAX.

## Input Format
- A string `s`.

## Example
**Input:** s = "   -42"  
**Output:** -42
