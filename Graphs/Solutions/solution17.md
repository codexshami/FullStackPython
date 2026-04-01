# Solution 17: The Word Ladder (Word Ladder)

## Approach Explanation
We treat each word as a node and connect words that differ by one letter. We use BFS to find the shortest path from `beginWord` to `endWord`.

## Step-by-Step Logic
1. Build a dictionary of patterns: for each word, create patterns by replacing each character with `*`.
2. BFS from `beginWord`.
3. For each word, find all neighbors by checking patterns.
4. Track the level (transformation count).
5. When we reach `endWord`, return the level.

## Complexity
- **Time Complexity:** O(M^2 * N) where M is word length, N is word count.
- **Space Complexity:** O(M^2 * N).

## Code
```python
from collections import deque, defaultdict

def ladder_length(begin_word, end_word, word_list):
    if end_word not in word_list:
        return 0
    
    word_set = set(word_list)
    queue = deque([(begin_word, 1)])
    visited = set([begin_word])
    
    while queue:
        word, level = queue.popleft()
        
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = word[:i] + c + word[i+1:]
                if next_word == end_word:
                    return level + 1
                if next_word in word_set and next_word not in visited:
                    visited.add(next_word)
                    queue.append((next_word, level + 1))
    
    return 0
```
