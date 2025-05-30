# Last updated: 5/30/2025, 12:07:49 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        diameter = [0]
        
        def dfs(node):
            if not node:
                return -1
            
            left = dfs(node.left)
            right = dfs(node.right)
            diameter[0] = max(diameter[0], 2 + left + right)
            
            return 1 + max(left, right)
        
        dfs(root)
        return diameter[0]
            