# 994. Rotting Oranges

from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        count = 0
        rotten_queue: deque[tuple[int, int]] = deque()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    rotten_queue.append((row, col))
                elif grid[row][col] == 1:
                    count += 1

        minutes = 0

        while rotten_queue and count > 0:
            minutes += 1

            # Need to go through one round of simulation first and then add minutes
            for _ in range(len(rotten_queue)):
                row, col = rotten_queue.popleft()

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 1:
                        count -= 1
                        grid[r][c] = 2
                        rotten_queue.append((r, c))

        return minutes if count == 0 else -1


sol = Solution()
res = sol.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]])
print(res)
