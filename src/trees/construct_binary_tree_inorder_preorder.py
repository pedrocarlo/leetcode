# 105. Construct Binary Tree from Preorder and Inorder Traversal

# Definition for a binary tree node.

from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # O(n**2) recursive simpler
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorder = deque(preorder)

        def helper(preorder: deque[int], inorder: List[int]):
            if not inorder:
                return None
            idx = inorder.index(preorder.popleft())
            root = TreeNode(inorder[idx])

            root.left = helper(preorder, inorder[:idx])
            root.right = helper(preorder, inorder[idx + 1 :])

            return root

        return helper(preorder, inorder)

    # O(n)
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        mapping = {}

        # register value to index before
        for i in range(len(inorder)):
            mapping[inorder[i]] = i

        preorder = deque(preorder)

        def build(start, end):
            if start > end:
                return None

            root = TreeNode(preorder.popleft())
            mid = mapping[root.val]

            root.left = build(start, mid - 1)
            root.right = build(mid + 1, end)

            return root

        return build(0, len(preorder) - 1)
