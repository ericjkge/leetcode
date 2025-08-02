# Last updated: 8/2/2025, 11:44:14 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def dfs(node):
            if not node:
                return -1

            lheight = dfs(node.left)
            rheight = dfs(node.right)
            self.ans = max(self.ans, lheight + rheight + 2)

            return max(lheight, rheight) + 1

        dfs(root)
        return self.ans
