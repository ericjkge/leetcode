# Last updated: 8/1/2025, 5:15:02 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.max_depth = 0
        self.ans = root
        
        def dfs(node, depth):
            if not node:
                return
            
            if depth > self.max_depth:
                self.max_depth = depth
                self.ans = node
            
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        
        dfs(root, 0)
        return self.ans.val
        