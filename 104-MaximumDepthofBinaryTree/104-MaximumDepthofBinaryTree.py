# Last updated: 7/24/2026, 10:23:20 PM
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
13            left, right = dfs(node.left), dfs(node.right)
14            return 1 + max(left, right)
15        
16        return dfs(root)