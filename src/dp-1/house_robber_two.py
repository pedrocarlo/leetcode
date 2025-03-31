# 213. House Robber II

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def dp_max(nums: List[int]):
            n = len(nums)
            dp = [0] * (n + 1)
            dp[0] = 0
            dp[1] = nums[0]
            for i in range(1, n):
                dp[i + 1] = max(dp[i], dp[i - 1] + nums[i])
            return dp[n]

        # insight here is to remove first and last and compute dp for both
        return max(dp_max(nums[1:]), dp_max(nums[:-1]))


sol = Solution()
res = sol.rob([2, 3, 2])
print(res)
