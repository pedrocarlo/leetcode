# 46. Permutations

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.n = len(nums)
        self.output = []
        self.backtrack([], nums)
        return self.output

    def backtrack(self, curr: list[int], nums: list[int]):
        if len(curr) == self.n:
            self.output.append(curr[:])
            return

        for i in range(self.n):
            if nums[i] in curr:
                continue
            curr.append(nums[i])
            self.backtrack(curr, nums)
            curr.pop()
