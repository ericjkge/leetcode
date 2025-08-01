# Last updated: 8/1/2025, 10:31:19 PM
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
            if not node.left and not node.right:
                if total == targetSum:
                    return True
                return False
            
            return dfs(node.left, total) or dfs(node.right, total)
        
        return dfs(root, 0)

            
