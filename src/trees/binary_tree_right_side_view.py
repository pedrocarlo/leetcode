# 199. Binary Tree Right Side View

# Definition for a binary tree node.

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: TreeNode | None = left
        self.right: TreeNode | None = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        if root is None:
            return ret

        def helper(root: Optional[TreeNode], depth: int):
            if root is None:
                return
            if depth == len(ret):
                ret.append(root.val)
            helper(root.right, depth + 1)
            helper(root.left, depth + 1)

        helper(root, 0)
        return ret
