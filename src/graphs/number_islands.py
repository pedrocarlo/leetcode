# 200. Number of Islands

from typing import List
from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def bfs(row: int, col: int):
            queue: deque[tuple[int, int]] = deque()
            visited.add((row, col))
            queue.append((row, col))

            while queue:
                row, col = queue.popleft()

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (
                        0 <= r < rows
                        and 0 <= c < cols
                        and grid[r][c] == "1"
                        and (r, c) not in visited
                    ):
                        queue.append((r, c))
                        visited.add((r, c))

        for row in range(rows):
            for col in range(cols):
                if (row, col) not in visited and grid[row][col] == "1":
                    islands += 1
                    bfs(row, col)
        return islands
