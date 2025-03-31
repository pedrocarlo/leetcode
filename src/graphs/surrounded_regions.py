# 130. Surrounded Regions
from typing import List
from collections import deque


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        visited = set()

        def bfs(row: int, col: int) -> tuple[List[tuple[int, int]], bool]:
            region = set([(row, col)])
            queue = deque([(row, col)])
            visited.add((row, col))
            has_border = False

            if row == 0 or row == rows - 1 or col == 0 or col == cols - 1:
                has_border = True

            while queue:
                row, col = queue.popleft()

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (
                        (r, c) not in region
                        and (r, c) not in visited
                        and (0 <= r < rows)
                        and (0 <= c < cols)
                        and board[r][c] == "O"
                    ):
                        region.add((r, c))
                        visited.add((r, c))
                        queue.append((r, c))

                        if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                            has_border = True
            return list(region), has_border

        for row in range(1, rows - 1):
            for col in range(1, cols - 1):
                if board[row][col] == "O" and (row, col) not in visited:
                    region, has_border = bfs(row, col)
                    if not has_border:
                        for r, c in region:
                            board[r][c] = "X"


sol = Solution()
# arr = [
#     ["X", "X", "X", "X"],
#     ["X", "O", "O", "X"],
#     ["X", "X", "O", "X"],
#     ["X", "O", "X", "X"],
# ]
# res = sol.solve(arr)
# print(arr)

arr = [
    ["X", "O", "X", "O", "X", "O"],
    ["O", "X", "O", "X", "O", "X"],
    ["X", "O", "X", "O", "X", "O"],
    ["O", "X", "O", "X", "O", "X"],
]
res = sol.solve(arr)
print(arr)
