# 215. Kth Largest Element in an Array

from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-x for x in nums]
        heapq.heapify(heap)
        val = 0
        for i in range(k):
            val = heapq.heappop(heap)

        return -val


sol = Solution()
res = sol.findKthLargest([3, 2, 1, 5, 6, 4], 2)
print(res)
