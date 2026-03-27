# Solution 10: Task Orchestration

## Approach Explanation
We sort the tasks by their enqueue time. We use a Min-Heap to store the tasks that are available (enqueued) but not yet processed. The heap is sorted by `processingTime` and then by the original `index`.

## Step-by-Step Logic
1. Add the original index to each task.
2. Sort tasks by `enqueueTime`.
3. Initialize `time = 0`, `res = []`, and a `min_heap`.
4. While there are tasks remaining or the heap is not empty:
   - If the heap is empty and `time < next_task_enqueueTime`, jump `time` to `next_task_enqueueTime`.
   - Push all tasks into the heap whose `enqueueTime <= time`.
   - Pop the best task from the heap, update `time`, and add index to `res`.
5. Return `res`.

## Complexity
- **Time Complexity:** O(N log N).
- **Space Complexity:** O(N).

## Code
```python
import heapq

def get_order(tasks):
    # original_idx, enq_time, proc_time
    sorted_tasks = sorted([(t[0], t[1], i) for i, t in enumerate(tasks)])
    res = []
    min_heap = []
    
    time = sorted_tasks[0][0]
    i = 0
    while i < len(tasks) or min_heap:
        # Add tasks to heap that are available at current time
        while i < len(tasks) and sorted_tasks[i][0] <= time:
            heapq.heappush(min_heap, (sorted_tasks[i][1], sorted_tasks[i][2]))
            i += 1
            
        if not min_heap:
            # CPU idle, jump to the next task's enqueue time
            time = sorted_tasks[i][0]
        else:
            # Process the shortest task
            proc_time, idx = heapq.heappop(min_heap)
            time += proc_time
            res.append(idx)
            
    return res
```
