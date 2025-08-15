# Last updated: 8/16/2025, 12:21:11 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        ans = []
        
        def dfs(node):
            if not node:
                return
            ans.append(str(node.val))
            if node.left or node.right:
                ans.append("(")
                dfs(node.left)
                ans.append(")")
            if node.right:
                ans.append("(")
                dfs(node.right)
                ans.append(")")
        
        dfs(root)
        return "".join(ans)