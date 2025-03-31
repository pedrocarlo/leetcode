# 417. Pacific Atlantic Water Flow

from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        pacific = set()
        atlantic = set()

        def dfs(row: int, col: int, curr_set: set, prev_height: int):
            if (
                row < 0
                or row >= rows
                or col < 0
                or col >= cols
                or (row, col) in curr_set
                or heights[row][col] < prev_height
            ):
                return

            curr_set.add((row, col))

            for dr, dc in directions:
                dfs(row + dr, col + dc, curr_set, heights[row][col])

        for col in range(0, cols):
            dfs(0, col, pacific, heights[0][col])  # top row
            dfs(rows - 1, col, atlantic, heights[rows - 1][col])  # bottom row

        for row in range(0, rows):
            dfs(row, 0, pacific, heights[row][0])  # 1st col
            dfs(row, cols - 1, atlantic, heights[row][cols - 1])  # last col

        return [[r, c] for r, c in pacific & atlantic]


sol = Solution()
res = sol.pacificAtlantic(
    [
        [1, 2, 2, 3, 5],
        [3, 2, 3, 4, 4],
        [2, 4, 5, 3, 1],
        [6, 7, 1, 4, 5],
        [5, 1, 1, 2, 4],
    ]
)
print(res)
