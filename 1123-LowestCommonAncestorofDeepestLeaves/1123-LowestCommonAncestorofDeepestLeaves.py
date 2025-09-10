# Last updated: 9/10/2025, 12:22:05 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return 0, None
            
            lheight, llca = dfs(node.left)
            rheight, rlca = dfs(node.right)

            if lheight > rheight:
                return 1 + lheight, llca
            if lheight < rheight:
                return 1 + rheight, rlca
            return 1 + lheight, node

        return dfs(root)[1]