# 235. Lowest Common Ancestor of a Binary Search Tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x: int):
        self.val = x
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        # Invariant p < q
        if p.val > q.val:
            p, q = q, p

        def helper(root: "TreeNode"):
            if p.val <= root.val <= q.val:
                return root
            if p.val < root.val and q.val < root.val:
                return helper(root.left)
            return helper(root.right)

        return helper(root)
