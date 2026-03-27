# Solution 17: Persistent Binary State

## Approach Explanation
We use level-order traversal (BFS) to represent the tree as a comma-separated string of values, including "None" for null pointers. During deserialization, we use a queue to reconstruct the tree level by level.

## Step-by-Step Logic
1. `serialize(root)`:
   - Use a queue for BFS.
   - Append `str(node.val)` if node exists, else "None".
   - Return combined string.
2. `deserialize(data)`:
   - Split string and handle empty case.
   - Create `root` from the first element.
   - Use a queue to keep track of parent nodes.
   - For each parent, assign the next two values in the array as its `left` and `right` children, then push them to the queue if they are not None.

## Complexity
- **Time Complexity:** O(N) for both.
- **Space Complexity:** O(N).

## Code
```python
from collections import deque

class Codec:
    def serialize(self, root):
        if not root: return ""
        q = deque([root])
        res = []
        while q:
            node = q.popleft()
            if node:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                res.append("None")
        return ",".join(res)

    def deserialize(self, data):
        if not data: return None
        nodes = data.split(",")
        root = TreeNode(int(nodes[0]))
        q = deque([root])
        i = 1
        while q:
            node = q.popleft()
            # Handle left child
            if nodes[i] != "None":
                node.left = TreeNode(int(nodes[i]))
                q.append(node.left)
            i += 1
            # Handle right child
            if nodes[i] != "None":
                node.right = TreeNode(int(nodes[i]))
                q.append(node.right)
            i += 1
        return root
```
