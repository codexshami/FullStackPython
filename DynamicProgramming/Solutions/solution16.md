# Solution 16: The Stock Trader (Best Time to Buy and Sell Stock with Cooldown)

## Approach Explanation
We define three states: `hold` (holding a stock), `sold` (just sold), `rest` (cooldown). We transition between states each day.

## Step-by-Step Logic
1. `hold[i]` = max(hold[i-1], rest[i-1] - prices[i]) — keep holding or buy.
2. `sold[i]` = hold[i-1] + prices[i] — sell the stock.
3. `rest[i]` = max(rest[i-1], sold[i-1]) — do nothing or come from cooldown.
4. Return max(sold[n-1], rest[n-1]).

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(1).

## Code
```python
def max_profit(prices):
    if not prices:
        return 0
    
    hold = -prices[0]
    sold = 0
    rest = 0
    
    for i in range(1, len(prices)):
        prev_hold = hold
        hold = max(hold, rest - prices[i])
        rest = max(rest, sold)
        sold = prev_hold + prices[i]
    
    return max(sold, rest)
```
