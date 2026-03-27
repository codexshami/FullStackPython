# Problem 2: Instant Minimum Access

## Problem Statement
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time. Implement the `MinStack` class.

## Input Format
- Method calls.

## Constraints
- -2^31 <= val <= 2^31 - 1
- At most 3 * 10^4 calls will be made to various methods.

## Example
**Input:** ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"] [[], [-2], [0], [-3], [], [], [], []]  
**Output:** [null, null, null, null, -3, null, 0, -2]
