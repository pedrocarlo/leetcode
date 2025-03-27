# 74. Search a 2D Matrix

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        total_len = m * n

        left = 0
        right = total_len - 1

        while left <= right:
            mid = (right + left) // 2
            col_idx = mid % n
            row_idx = mid // n
            print(col_idx, row_idx, left, right)
            if row_idx >= m or col_idx >= n:
                return False
            val = matrix[row_idx][col_idx]
            if val == target:
                return True
            if val > target:
                right = mid - 1
            else:
                left = mid + 1

        return False


sol = Solution()
# res = sol.searchMatrix([[1,1]], 2)
# print(res)

# res = sol.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3)
# print(res)

res = sol.searchMatrix([[1, 3]], 3)
print(res)
