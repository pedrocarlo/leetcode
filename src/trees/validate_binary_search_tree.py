# 98. Validate Binary Search Tree


# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: Optional[TreeNode] = left
        self.right: Optional[TreeNode] = right


# in order traversal (DFS) and check before setting the prev element
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        stack: list[TreeNode] = []
        prev: Optional[TreeNode] = None
        while root is not None or stack:
            while root is not None:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if prev is not None and root.val <= prev.val:
                return False
            prev = root
            root = root.right
        
        return True

    # recursive simple approach
    def isValidBST(self, root: Optional[TreeNode]) -> bool:  # noqa: F811
        elements = []

        def inorder(node, elements):
            if node is None:
                return
            inorder(node.left, elements)
            elements.append(node.val)
            inorder(node.right, elements)

        inorder(root, elements)
        for i in range(1, len(elements)):
            if elements[i - 1] >= elements[i]:
                return False
        return True
