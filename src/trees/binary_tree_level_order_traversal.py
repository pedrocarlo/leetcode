# 102. Binary Tree Level Order Traversal


# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: TreeNode | None = left
        self.right: TreeNode | None = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # classic bst
        if root is None:
            return []
        visited = set()
        ret = [[]]
        prev_level = 0
        queue = [(root, 0)]
        while queue:
            (node, curr_level) = queue.pop(0)
            visited.add(node)
            if prev_level != curr_level:
                ret.append([])
                prev_level = curr_level
            ret[curr_level].append(node.val)

            nodes = [node.left, node.right]
            for node in nodes:
                if node not in visited and node is not None:
                    queue.append((node, curr_level + 1))

        return ret
