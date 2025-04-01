# https://www.fastprep.io/problems/citadel-get-max-throughput


from typing import List


# claude answer again
class Solution:
    def getMaxThroughput(
        self, throughput: List[int], scaling_cost: List[int], budget: int
    ) -> int:
        n = len(throughput)

        # Helper function to check if we can achieve a target throughput within budget
        def can_achieve_throughput(target):
            total_cost = 0

            for i in range(n):
                base = throughput[i]

                if base >= target:
                    # No scaling needed
                    continue

                # We need to find x such that: base * (1 + x) >= target
                # Solving for x: (1 + x) >= target / base
                # x >= (target / base) - 1

                # Since x must be an integer and we need >= target throughput,
                # we need to ceiling the result
                # This is equivalent to: ceil(target/base) - 1

                # Ceiling division formula: (a + b - 1) // b gives ceil(a/b)
                x = (target + base - 1) // base - 1

                total_cost += x * scaling_cost[i]

                if total_cost > budget:
                    return False

            return True

        # Binary search for the maximum achievable throughput
        left = 1
        # A reasonable upper bound
        right = max(throughput) * (budget + 1)  # This should be large enough

        result = 0

        while left < right:
            mid = (left + right) // 2

            if can_achieve_throughput(mid):
                # We can achieve this throughput, save it and try higher
                result = mid
                left = mid + 1
            else:
                # Cannot achieve this throughput, try lower
                right = mid

        return result


sol = Solution()
res = sol.getMaxThroughput([4, 2, 7], [3, 5, 6], 32)
# 10
print(res)

res = sol.getMaxThroughput([7, 3, 4, 6], [2, 5, 4, 3], 25)
# 9
print(res)
