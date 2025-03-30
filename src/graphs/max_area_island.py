# 695. Max Area of Island

from typing import List
from collections import deque


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_island = 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

        def bfs(row: int, col: int) -> int:
            queue = deque()
            visited.add((row, col))
            queue.append((row, col))
            count = 0

            while queue:
                row, col = queue.popleft()
                count += 1

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (
                        0 <= r < rows
                        and 0 <= c < cols
                        and (r, c) not in visited
                        and grid[r][c] == 1
                    ):
                        visited.add((r, c))
                        queue.append((r, c))
            return count

        for row in range(rows):
            for col in range(cols):
                if (row, col) not in visited and grid[row][col] == 1:
                    max_island = max(max_island, bfs(row, col))

        return max_island
