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

    # bitmask approach
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = []

        for i in range(2**n, 2 ** (n + 1)):
            # generate bitmask, from 0..00 to 1..11
            bitmask = bin(i)[3:]

            # append subset corresponding to that bitmask
            output.append([nums[j] for j in range(n) if bitmask[j] == "1"])

        return output