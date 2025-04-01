# 152. Maximum Product Subarray

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * (n + 1)
        dp[1] = nums[0]
        largest_product = 0

        for i in range(n):
            dp[i] = max(dp[i - 1], dp[i - 1] * nums[i])
            largest_product = max(largest_product, dp[i])
        print(dp)
        return largest_product


sol = Solution()
res = sol.maxProduct([2, 3, -2, 4])
# 6
print(res)


# kadane algorithm but with min together
def maxProduct(self, nums: list[int]):
    n = len(nums)
    Max = nums[0]
    Min = nums[0]
    product = nums[0]

    for i in range(1, n):
        curr = nums[i]

        if curr < 0:
            Max, Min = Min, Max

        Max = max(curr, Max * curr)
        Min = min(curr, Min * curr)
        product = max(product, Max)

    return product
