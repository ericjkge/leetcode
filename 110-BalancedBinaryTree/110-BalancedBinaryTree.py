# Last updated: 9/9/2025, 3:41:57 PM
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
                return 0, True

            ldepth, lbalanced = dfs(node.left)            
            rdepth, rbalanced = dfs(node.right)

            return max(ldepth, rdepth) + 1, (abs(ldepth - rdepth) <= 1 and lbalanced and rbalanced)
        
        return dfs(root)[1]