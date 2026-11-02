# Last updated: 11/2/2026, 4:39:45 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxDepth(self, root: TreeNode | None) -> int:
9        def dfs(node):
10            if node is None:
11                return 0
12            
13            left = dfs(node.left)
14            right = dfs(node.right)
15            return 1 + max(left, right)
16        
17        return dfs(root)