# Solution 6: The Coin Puzzle (Coin Change)

## Approach Explanation
We use bottom-up DP. `dp[i]` represents the minimum number of coins needed to make amount `i`. We try each coin and take the minimum.

## Step-by-Step Logic
1. Create `dp` array of size `amount + 1`, initialized to infinity.
2. `dp[0] = 0` (0 coins for amount 0).
3. For each amount from 1 to target:
   - For each coin: if `coin <= amount`, `dp[amount] = min(dp[amount], dp[amount - coin] + 1)`.
4. Return `dp[amount]` if reachable, else -1.

## Complexity
- **Time Complexity:** O(amount * len(coins)).
- **Space Complexity:** O(amount).

## Code
```python
def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1
```
