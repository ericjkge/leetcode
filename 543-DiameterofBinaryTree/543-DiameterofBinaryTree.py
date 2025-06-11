# Last updated: 6/10/2025, 11:37:01 PM
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
            left = dfs(node.left)
            right = dfs(node.right)
            
            height = max(left, right) + 1
            self.ans = max(self.ans, left + right + 2)
            return height
        
        dfs(root)
        return self.ans