# Last updated: 7/26/2025, 10:24:44 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.max_depth = 0

        def dfs(root, depth):
            if not root:
                return
            
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)

            if depth > self.max_depth:
                self.max_depth = depth
                self.ans = root.val
        
        dfs(root, 1)
        return self.ans