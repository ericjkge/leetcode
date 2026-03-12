# Last updated: 3/11/2026, 11:38:21 PM
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
13            left = dfs(node.left)
14            right = dfs(node.right)
15            return 1 + max(left, right)
16        
17        return dfs(root)