# Solution 8: Serpentine Dynamics (Snake Game Design)

## Approach Explanation
We use a `deque` (double-ended queue) to store the body coordinates of the snake. The front of the deque is the head. We also use a hash set to store the body parts for O(1) crash detection.

## Step-by-Step Logic
1. `__init__`: Store `width`, `height`, `food` list, and initialize `snake = deque([(0,0)])`, `body = set([(0,0)])`, `food_idx = 0`.
2. `move(direction)`:
   - Calculate new head position berdasarkan `direction`.
   - Check wall collision. If yes, return -1.
   - Check if new head is at `food[food_idx]`.
     - If yes, increment `food_idx` and `score`. Don't pop tail.
     - If no, pop tail from `snake` and `body`.
   - Check body collision (is new head in `body`?). If yes, return -1.
   - Add new head to `snake` and `body`.
   - Return `score`.

## Complexity
- **Time Complexity:** O(1) per move.
- **Space Complexity:** O(N + L), where N is snake length and L is food count.

## Code
```python
from collections import deque

class SnakeGame:
    def __init__(self, width: int, height: int, food: list[list[int]]):
        self.w, self.h = width, height
        self.food = food
        self.food_idx = 0
        self.snake = deque([(0, 0)])
        self.body = {(0, 0)}
        self.dir_map = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

    def move(self, direction: str) -> int:
        r, c = self.snake[0]
        dr, dc = self.dir_map[direction]
        nr, nc = r + dr, c + dc
        
        # 1. Wall collision
        if not (0 <= nr < self.h and 0 <= nc < self.w):
            return -1
            
        # 2. Food check
        has_food = (self.food_idx < len(self.food) and 
                    [nr, nc] == self.food[self.food_idx])
        
        if not has_food:
            tail = self.snake.pop()
            self.body.remove(tail)
            
        # 3. Body collision
        if (nr, nc) in self.body:
            return -1
            
        self.snake.appendleft((nr, nc))
        self.body.add((nr, nc))
        
        if has_food:
            self.food_idx += 1
            
        return len(self.snake) - 1
```
