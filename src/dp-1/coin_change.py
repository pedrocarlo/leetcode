# 322. Coin Change

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = amount
        dp = [float("inf")] * (n + 1)
        dp[0] = 0

        # Iterate through each coin denomination
        for coin in coins:
            # Iterate through all amounts from the current coin value to the target amount
            for x in range(coin, n + 1):
                # Update dp[x] with the minimum of:
                # 1. The current value of dp[x] (minimum coins needed without considering the current coin)
                # 2. dp[x - coin] + 1 (minimum coins needed for the remaining amount (x - coin) plus the current coin)
                dp[x] = min(dp[x], dp[x - coin] + 1)

        return dp[n] if dp[n] != float("inf") else -1


sol = Solution()
res = sol.coinChange([1, 2, 5], 11)
print(res)
