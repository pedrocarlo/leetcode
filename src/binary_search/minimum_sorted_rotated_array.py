# 153. Find Minimum in Rotated Sorted Array

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            # print(left, right, mid)
            if nums[mid] <= nums[right]:
                right = mid
            else:
                left = mid + 1

        # print(left, right)
        return nums[left]


sol = Solution()
# res = sol.findMin([3, 4, 5, 1, 2])
# print(res)

# res = sol.findMin([4, 5, 6, 7, 0, 1, 2])
# print(res)

# res = sol.findMin([11, 13, 15, 17])
# print(res)
