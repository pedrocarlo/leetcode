# 543. Diameter of Binary Tree

# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def inorder(root: Optional[TreeNode]) -> int:
            nonlocal res
            if root is None:
                return 0

            left = inorder(root.left)

            right = inorder(root.right)

            res = max(res, left + right)

            return max(left, right) + 1
        inorder(root)
        return res
