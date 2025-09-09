# Last updated: 9/9/2025, 1:20:19 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.max_depth = -1

        def dfs(node, depth):
            if not node:
                return
            
            if depth > self.max_depth:
                self.max_depth = depth
                self.ans = node.val

            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        
        dfs(root, 0)
        return self.ans