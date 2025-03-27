# 704. Binary Search

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (right + left) // 2
            if nums[mid] == target:
                return mid      
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1
    
sol = Solution()

res = sol.search([-1,0,3,5,9,12], 9)
print(res)