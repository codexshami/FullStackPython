# Solution 15: The Flattening Force (Flatten Nested List)

## Approach Explanation
We iterate through each element. If the element is a list, we recursively flatten it; otherwise, we append the integer to our result.

## Step-by-Step Logic
1. Initialize an empty result list.
2. Iterate through each element in the nested list.
3. If the element is a list, extend the result with the recursive flatten call.
4. If the element is an integer, append it directly.
5. Return the result.

## Complexity
- **Time Complexity:** O(N), where N is the total number of integers.
- **Space Complexity:** O(D), where D is the maximum nesting depth.

## Code
```python
def flatten(nested_list):
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result
```
