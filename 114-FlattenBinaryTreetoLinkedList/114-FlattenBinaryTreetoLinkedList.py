# Last updated: 9/8/2025, 7:06:31 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.prev = None

        def dfs(node):
            if not node:
                return
            
            if self.prev:
                self.prev.right = node
                self.prev.left = None

            self.prev = node

            right = node.right
            dfs(node.left)
            dfs(right)
        
        dfs(root)