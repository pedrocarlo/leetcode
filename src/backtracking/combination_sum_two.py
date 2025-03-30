# 40. Combination Sum II


from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.output = []
        self.n = len(candidates)
        candidates.sort()
        self.backtrack(0, [], candidates, target)
        return self.output

    def backtrack(
        self,
        start: int,
        curr: list[int],
        nums: List[int],
        target: int,
    ):
        if target < 0:
            return
        if target == 0 and curr:
            self.output.append(list(curr))
            return
        for i in range(start, self.n):
            if i > start and nums[i] == nums[i - 1]:
                continue
            curr.append(nums[i])
            self.backtrack(i + 1, curr, nums, target - nums[i])
            curr.pop()
