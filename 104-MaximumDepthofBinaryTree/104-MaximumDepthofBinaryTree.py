# Last updated: 1/28/2026, 9:34:21 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxDepth(self, root: Optional[TreeNode]) -> int:
9        def dfs(node):
10            if not node:
11                return 0
12            
13            return 1 + max(dfs(node.left), dfs(node.right))
14        
15        return dfs(root)