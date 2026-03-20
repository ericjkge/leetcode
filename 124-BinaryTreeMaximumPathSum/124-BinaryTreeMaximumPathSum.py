# Last updated: 3/20/2026, 3:26:16 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxPathSum(self, root: Optional[TreeNode]) -> int:
9        self.path = float("-inf")
10
11        def dfs(node):
12            if not node:
13                return 0
14            
15            left = dfs(node.left)
16            right = dfs(node.right)
17            
18            self.path = max(self.path, left + right + node.val, left + node.val, right + node.val, node.val)
19
20            return node.val + max(left, right, 0)
21        
22        dfs(root)
23        return self.path