# Last updated: 8/2/2025, 11:48:08 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self.longest = 0
        
        def dfs(node, prev, length):
            if not node:
                return
            
            if node == root or node.val == prev + 1:
                length += 1
            else:
                length = 1
            
            if length > self.longest:
                self.longest = length
            
            dfs(node.left, node.val, length)
            dfs(node.right, node.val, length)
        
        dfs(root, 0, 0)
        return self.longest