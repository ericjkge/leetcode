# Last updated: 11/27/2025, 9:20:58 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def flatten(self, root: Optional[TreeNode]) -> None:
9        """
10        Do not return anything, modify root in-place instead.
11        """
12        self.prev = None
13
14        def dfs(node):
15            if not node:
16                return
17            
18            if self.prev:
19                self.prev.left = None
20                self.prev.right = node
21            
22            self.prev = node
23            right = node.right
24            dfs(node.left)
25            dfs(right)
26        
27        dfs(root)