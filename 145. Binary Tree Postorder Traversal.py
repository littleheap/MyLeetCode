# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:

        if not root:
            return []

        res = []

        def post(node):
            if not node:
                return
            else:
                post(node.left)
                post(node.right)
                res.append(node.val)

        post(root)
        return res
