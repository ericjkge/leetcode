# Last updated: 9/9/2025, 7:29:12 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, total):
            if not node:
                return False
            
            total += node.val
            
            if total == targetSum and not node.left and not node.right:
                return True
            
            return dfs(node.left, total) or dfs(node.right, total)
        
        return dfs(root, 0)