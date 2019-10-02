# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        if not root:
            return True
        res = []

        def deep(node):
            if node is None:
                return
            else:
                deep(node.left)
                res.append(node.val)
                deep(node.right)

        deep(root)
        for i in range(1, len(res)):
            if res[i] <= res[i - 1]:
                return False
        return True
