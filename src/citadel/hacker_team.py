# https://www.fastprep.io/problems/hackers-team


from typing import List
import heapq


class Solution:
    def getMaxSubarrayLen(self, team_a: List[int], team_b: List[int]) -> int:
        n = len(team_a)

        # Try all possible subarrays
        max_length = 0

        for i in range(n):
            # For each starting position, find the maximum possible length

            # We'll use a BFS approach to explore all possible paths
            queue = [(i, team_a[i]), (i, team_b[i])]  # (position, skill)
            visited = set(queue)
            max_end = i  # Maximum reachable end

            while queue:
                pos, skill = queue.pop(0)

                # Update the maximum reachable end
                max_end = max(max_end, pos)

                # Try to extend to the next position
                next_pos = pos + 1
                if next_pos < n:
                    # Try team_a[next_pos]
                    if (
                        team_a[next_pos] >= skill
                        and (next_pos, team_a[next_pos]) not in visited
                    ):
                        queue.append((next_pos, team_a[next_pos]))
                        visited.add((next_pos, team_a[next_pos]))

                    # Try team_b[next_pos]
                    if (
                        team_b[next_pos] >= skill
                        and (next_pos, team_b[next_pos]) not in visited
                    ):
                        queue.append((next_pos, team_b[next_pos]))
                        visited.add((next_pos, team_b[next_pos]))

            # Update the maximum length
            max_length = max(max_length, max_end - i + 1)

        return max_length


sol = Solution()
res = sol.getMaxSubarrayLen([5, 2, 4, 1], [3, 6, 2, 2])
# 3
print(res)
