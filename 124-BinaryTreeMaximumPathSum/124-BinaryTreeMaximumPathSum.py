# Last updated: 2/22/2026, 9:17:03 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxPathSum(self, root: Optional[TreeNode]) -> int:
9        self.max = float("-inf")
10
11        def dfs(node):
12            if not node:
13                return 0
14        
15            left = dfs(node.left)
16            right = dfs(node.right)
17            self.max = max(self.max, left + node.val + right, left + node.val, right + node.val, node.val)
18
19            return node.val + max(left, right, 0)
20
21        dfs(root)
22        return self.max