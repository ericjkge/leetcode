# Last updated: 9/11/2025, 12:34:21 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self.longest = 0

        def dfs(node, prev, path):
            if not node:
                return
            
            if prev == None or node.val == prev + 1:
                path += 1
                self.longest = max(self.longest, path)
            else:
                path = 1

            dfs(node.left, node.val, path)
            dfs(node.right, node.val, path)
            return

        dfs(root, None, 0)
        return self.longest