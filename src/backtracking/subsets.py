# 78. Subsets

from typing import List


class Solution:
    # Iterative approach
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = [[]]
        for num in nums:
            temp = []
            for s in ret:
                temp.append(s + [num])

            ret += list(temp)
        return list(ret)

    # backtracking
    def subsets(self, nums):
        self.output = []
        self.n = len(nums)
        self.backtrack(0, [], nums)
        return self.output

    def backtrack(self, first: int, curr: list[int], nums):
        # Add the current subset to the output
        self.output.append(curr[:])
        # Generate subsets starting from the current index
        for i in range(first, self.n):
            curr.append(nums[i])
            self.backtrack(i + 1, curr, nums)
            curr.pop()