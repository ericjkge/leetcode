# Last updated: 7/5/2025, 10:35:30 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return (True, 0)
            lbalance, lheight = dfs(node.left)
            rbalance, rheight = dfs(node.right)
            return (lbalance and rbalance and abs(lheight-rheight) < 2, max(lheight, rheight) + 1)
        
        return dfs(root)[0]