# 39. Combination Sum

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # backtracking
        self.output = []
        self.n = len(candidates)
        self.backtrack(0, [], candidates, target)
        return self.output

    def backtrack(self, first: int, curr: list[int], nums: list[int], target: int):
        if target < 0:
            return
        if target == 0:
            # Add the current subset to the output
            self.output.append(curr[:])
            return
        # Generate subsets starting from the current index
        for i in range(first, self.n):
            curr.append(nums[i])
            # have to change here how you backtrack
            self.backtrack(i, curr, nums, target - nums[i])
            curr.pop()
