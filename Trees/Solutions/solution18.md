# Solution 18: Security Network (Cameras)

## Approach Explanation
This is a Greedy problem solved using DFS. A node can be in three states:
0: Not covered (needs parent or itself to have a camera).
1: Has a camera.
2: Covered by a camera (but doesn't have one).
We try to place cameras as high as possible.

## Step-by-Step Logic
1. Traverse bottom-up.
2. If a child is "not covered" (0), the parent MUST have a camera. Increment count. Return 1.
3. If a child has a camera (1), the parent is "covered" (2). Return 2.
4. Otherwise, return "not covered" (0).
5. If the root ends up "not covered", add one more camera.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(H).

## Code
```python
def min_camera_cover(root):
    self.ans = 0
    # 0: Not covered, 1: Has camera, 2: Covered
    def dfs(node):
        if not node: return 2
        l, r = dfs(node.left), dfs(node.right)
        
        if l == 0 or r == 0:
            self.ans += 1
            return 1
        if l == 1 or r == 1:
            return 2
        return 0
        
    if dfs(root) == 0:
        self.ans += 1
    return self.ans
```
