from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: Optional[TreeNode] = left
        self.right: Optional[TreeNode] = right


def inorderTraversal(root: TreeNode) -> List[int]:
    list_items = []
    if root is None:
        return list_items
    stack: list[TreeNode] = []
    while root is not None or not stack:
        while root is not None:
            stack.append(root)
            root = root.left
        root = stack.pop()
        list_items.append(root.val)
        root = root.right

    return list_items
