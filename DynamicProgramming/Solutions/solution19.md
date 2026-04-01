# Solution 19: The Unbounded Knapsack (Coin Change II — Number of Ways)

## Approach Explanation
`dp[j]` represents the number of ways to make amount `j`. We process coins one at a time (outer loop) to avoid counting permutations as different combinations.

## Step-by-Step Logic
1. Create `dp` array of size `amount + 1`, initialized to 0.
2. `dp[0] = 1` (one way to make amount 0: use no coins).
3. For each coin:
   - For each amount from `coin` to `amount`:
     - `dp[j] += dp[j - coin]`.
4. Return `dp[amount]`.

## Complexity
- **Time Complexity:** O(amount * len(coins)).
- **Space Complexity:** O(amount).

## Code
```python
def change(amount, coins):
    dp = [0] * (amount + 1)
    dp[0] = 1
    
    for coin in coins:
        for j in range(coin, amount + 1):
            dp[j] += dp[j - coin]
    
    return dp[amount]
```
