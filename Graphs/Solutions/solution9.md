# Solution 9: The Course Scheduler (Course Schedule)

## Approach Explanation
This is a cycle detection problem in a directed graph. If a cycle exists in the prerequisite graph, it's impossible to complete all courses. We use topological sort (Kahn's algorithm).

## Step-by-Step Logic
1. Build an adjacency list and compute in-degrees.
2. Add all nodes with in-degree 0 to a queue.
3. Process nodes: decrement in-degrees of their neighbors.
4. If in-degree becomes 0, add neighbor to queue.
5. If all nodes are processed, return True (no cycle). Otherwise, False.

## Complexity
- **Time Complexity:** O(V + E).
- **Space Complexity:** O(V + E).

## Code
```python
from collections import deque, defaultdict

def can_finish(num_courses, prerequisites):
    graph = defaultdict(list)
    in_degree = [0] * num_courses
    
    for a, b in prerequisites:
        graph[b].append(a)
        in_degree[a] += 1
    
    queue = deque([i for i in range(num_courses) if in_degree[i] == 0])
    count = 0
    
    while queue:
        node = queue.popleft()
        count += 1
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return count == num_courses
```
