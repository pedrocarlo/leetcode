# https://www.fastprep.io/problems/citadel-get-min-operations


from typing import List
import math


class Solution:
    def citadelGetMinOperations(self, executionTime: List[int], x: int, y: int) -> int:
        def can_do_jobs(operations: int):
            # As you need to remove y at every step,
            # Just remove y at the start and then check if we need to add to make
            # a certain executimeTime <= 0
            curr_ops = 0
            aux = [item - operations * y for item in executionTime]
            for num in aux:
                if num > 0:
                    # Here it is x - y because at each step we either subtract x or y.
                    # as we already subtracted y, we would need to add y again and then subtract x
                    # from num, which is equivalent to x - y
                    while num > 0:
                        num -= x - y
                        curr_ops += 1
                    # curr_ops += math.ceil(num / (x - y)) # faster simplified version
                    if curr_ops > operations:
                        return False
            return True

        left = 0
        right = math.ceil(max(executionTime) / y)

        while left < right:
            mid = left + (right - left) // 2
            if can_do_jobs(mid):
                right = mid
            else:
                left = mid + 1
        return right


sol = Solution()
res = sol.citadelGetMinOperations([3, 4, 1, 7, 6], 4, 2)
# 3
print(res)

res = sol.citadelGetMinOperations([3, 3, 6, 3, 9], 3, 2)
# 3
print(res)

res = sol.citadelGetMinOperations([2, 3, 5], 3, 1)
# 3
print(res)
