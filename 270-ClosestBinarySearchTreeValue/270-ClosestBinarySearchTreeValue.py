# Last updated: 9/15/2025, 12:13:30 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        self.closest = float("inf")

        def dfs(node):
            if not node:
                return

            if abs(target - node.val) < abs(target - self.closest):
                self.closest = node.val

            if abs(target - node.val) == abs(target - self.closest) and node.val < self.closest:
                self.closest = node.val

            if node.val < target:
                dfs(node.right)
            else:
                dfs(node.left)
        
        dfs(root)
        return self.closest