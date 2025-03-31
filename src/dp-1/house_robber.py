# 198. House Robber

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n + 1)
        dp[1] = nums[0]

        for i in range(1, n):
            dp[i + 1] = max(dp[i], dp[i - 1] + nums[i])

        return dp[n]


sol = Solution()
res = sol.rob([1, 2, 3, 1])
print(res)
