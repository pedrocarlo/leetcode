# 90. Subsets II

from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.n = len(nums)
        self.output = []
        nums.sort()
        self.backtrack(0, [], nums)
        return self.output

    def backtrack(self, start: int, curr: List[int], nums: List[int]):
        self.output.append(curr[:])

        for i in range(start, self.n):
            if i > start and nums[i - 1] == nums[i]:
                continue
            curr.append(nums[i])
            self.backtrack(i + 1, curr, nums)
            curr.pop()
