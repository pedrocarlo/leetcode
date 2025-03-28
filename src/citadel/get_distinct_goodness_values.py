# https://www.fastprep.io/problems/citadel-get-good-value

from typing import List


class Solution:
    def findMinimumEqualSum(self, arr: List[int]) -> List[int]:
        ret = [0]
        good_set = set()
        good_set.add(0)
        stack: list[tuple[int, int]] = [(0, 0)]

        # Naive
        for i in range(len(arr)):
            curr = arr[i]
            good_set.add(arr[i])

            while stack and stack[-1][0] <= arr[i]:
                val = stack.pop()
                good_set.add(val[1])
                curr |= val[1]

            stack.append((arr[i], curr))
            good_set.add(curr)

        ret = [val for val in good_set]
        ret.sort()

        return ret


sol = Solution()
res = sol.findMinimumEqualSum([4, 2, 4, 1])
# [0, 1, 2, 4, 6]
print(res)

res = sol.findMinimumEqualSum([3, 2, 4, 6])
# [0, 2, 3, 4, 6, 7]
print(res)

res = sol.findMinimumEqualSum([3, 5, 5, 1])
# [0, 1, 3, 5, 7]
print(res)
