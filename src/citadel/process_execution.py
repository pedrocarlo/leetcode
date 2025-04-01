# https://www.fastprep.io/problems/get-maximum-power


from typing import List


class Solution:
    def getMaximumPower(self, power: List[int]) -> int:
        n = len(power)
        if n == 1:
            return power[0]
        if n == 0:
            return 0
        dp = [0] * (n + 1)
        dp[1] = power[0]
        dp[2] = max(power[0], power[1])

        for i in range(1, n):
            dp[i + 1] = max(dp[i - 1] + power[i], dp[i])
        print(dp)

        return dp[n]


sol = Solution()
res = sol.getMaximumPower([3, 3, 3, 4, 4, 1, 8])
# 18
print(res)
