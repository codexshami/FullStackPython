# Problem 20: The Expression Builder (Expression Add Operators)

## Problem Statement
Given a string `num` that contains only digits and an integer `target`, return all possibilities to insert the binary operators `'+'`, `'-'`, and/or `'*'` between the digits of `num` so that the resultant expression evaluates to the target value.

## Input Format
- A string `num` of digits.
- An integer `target`.

## Constraints
- 1 <= num.length <= 10
- num consists of only digits.

## Example
**Input:** num = "123", target = 6  
**Output:** ["1*2*3","1+2+3"]

**Input:** num = "232", target = 8  
**Output:** ["2*3+2","2+3*2"]
