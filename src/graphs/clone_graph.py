# 133. Clone Graph


from typing import Optional
from collections import deque


"""
# Definition for a Node.
"""


class Node:
    def __init__(self, val=0, neighbors: Optional[list["Node"]] = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        # bfs
        if node is None:
            return node
        queue: deque[Node] = deque()
        queue.append(node)
        clones: dict[int, Node] = {node.val: Node(node.val, [])}

        while queue:
            curr = queue.popleft()
            curr_clone = clones[curr.val]

            for new_node in curr.neighbors:
                if new_node.val not in clones:
                    clones[new_node.val] = Node(new_node.val, [])
                    queue.append(new_node)

                curr_clone.neighbors.append(clones[new_node.val])

        return clones[node.val]
