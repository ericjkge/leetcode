# Last updated: 7/8/2025, 12:25:56 PM
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
            if not node.right and not node.left:
                if total == targetSum:
                    return True
                else:
                    return False
            return dfs(node.left, total) or dfs(node.right, total)
        
        return dfs(root, 0)


            
