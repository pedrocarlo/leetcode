# https://www.fastprep.io/problems/is-special


from typing import List

"""
Let me explain this solution:

Finding Diameters: The key insight is that we can find a diameter of a tree using two BFS traversals:

Start BFS from any node to find the farthest node (end1)
Start another BFS from end1 to find the other end of the diameter (end2)
The path between end1 and end2 is one diameter of the tree


Finding All Special Nodes: However, we need to find ALL endpoints of ALL diameters, not just one. To do this:

For each endpoint of the first diameter we found (end1 and all nodes at distance = diameter_length from end2)
Run a BFS from each of these potential endpoints
Find all nodes that are at maximum distance from any of these endpoints
All such nodes are special nodes


Handling Multiple Diameters: The solution accounts for multiple diameters by checking nodes at maximum distance from each identified endpoint.

For example, with the input from Example 1:

We'll find that nodes 4, 5, 6, and 7 are special as they're endpoints of diameters
All other nodes are not special

This solution has a time complexity of O(N²) in the worst case, where N is the number of nodes in the tree, because we might need to run BFS from multiple endpoints.
"""


# Claude helped a lot here
class Solution:
    def isSpecial(
        self, tree_nodes: int, tree_from: List[int], tree_to: List[int]
    ) -> List[int]:
        # Build an adjacency list to represent the tree
        graph = [[] for _ in range(tree_nodes + 1)]  # +1 because nodes are 1-indexed

        # Add edges to the graph (undirected)
        for i in range(len(tree_from)):
            graph[tree_from[i]].append(tree_to[i])
            graph[tree_to[i]].append(tree_from[i])

        # Function to find the farthest node from a given start node
        # Returns (farthest node, distance)
        def bfs(start):
            distances = [-1] * (tree_nodes + 1)
            distances[start] = 0

            queue = [start]
            while queue:
                node = queue.pop(0)
                for neighbor in graph[node]:
                    if distances[neighbor] == -1:  # Unvisited
                        distances[neighbor] = distances[node] + 1
                        queue.append(neighbor)

            # Find the farthest node and its distance
            farthest_node = 1
            max_distance = 0
            for i in range(1, tree_nodes + 1):
                if distances[i] > max_distance:
                    max_distance = distances[i]
                    farthest_node = i

            return farthest_node, max_distance, distances

        # Step 1: Pick any node (let's choose node 1) and find the farthest node from it
        end1, _, _ = bfs(1)

        # Step 2: From the farthest node (end1), find the other end of a diameter
        end2, diameter_length, distances_from_end2 = bfs(end1)

        # Step 3: Find all nodes that are exactly diameter_length distance away from end2
        # These are potential endpoints of other diameters
        potential_endpoints = []
        for i in range(1, tree_nodes + 1):
            if distances_from_end2[i] == diameter_length:
                potential_endpoints.append(i)

        # Mark all nodes that are at the maximum distance from any potential endpoint
        special_nodes = [0] * tree_nodes

        # Mark the endpoints we already found
        special_nodes[end1 - 1] = 1
        for endpoint in potential_endpoints:
            special_nodes[endpoint - 1] = 1

            # For each potential endpoint, find other nodes at max distance from it
            _, _, distances = bfs(endpoint)
            for i in range(1, tree_nodes + 1):
                if distances[i] == diameter_length:
                    special_nodes[i - 1] = 1

        return special_nodes


sol = Solution()
res = sol.isSpecial(7, [1, 2, 3, 3, 1, 1], [2, 3, 4, 5, 6, 7])
# [0, 0, 0, 1, 1, 1, 1]
print(res)
