# 1448. Count Good Nodes in Binary Tree

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: TreeNode | None = left
        self.right: TreeNode | None = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(root: Optional[TreeNode], prev_max: int):
            if root is None:
                return 0
            curr_max = max(prev_max, root.val)
            if root.val >= prev_max:
                return 1 + helper(root.left, curr_max) + helper(root.right, curr_max)
            return helper(root.left, curr_max) + helper(root.right, curr_max)

        return helper(root, float("-inf"))
