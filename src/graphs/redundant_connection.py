# 684. Redundant Connection

from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        visited = set()
        adj = [[] for _ in range(n + 1)]
        cycle_start = -1
        parent_map: dict[int, int] = {n: -1 for n in range(1, n + 1)}

        for first, second in edges:
            adj[first].append(second)
            adj[second].append(first)

        # bfs to build parent_map and detect where cycle start
        def dfs(curr: int):
            nonlocal cycle_start

            visited.add(curr)

            for node in adj[curr]:
                if node not in visited:
                    parent_map[node] = curr
                    dfs(node)
                elif cycle_start == -1 and node != parent_map[curr]:
                    cycle_start = node
                    parent_map[node] = curr

        dfs(1)

        # get all nodes that are in a cycle
        curr = cycle_start
        cycle_nodes = set()
        while True:
            cycle_nodes.add(curr)
            curr = parent_map[curr]
            if curr == cycle_start:
                break

        # reverse iterate to find last edge that both nodes are in a cycle together
        for i in range(n - 1, 1, -1):
            if edges[i][0] in cycle_nodes and edges[i][1] in cycle_nodes:
                return edges[i]


sol = Solution()
# res = sol.findRedundantConnection([[1, 2], [1, 3], [2, 3]])
# print(res)

res = sol.findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]])
print(res)
