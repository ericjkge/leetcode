# Last updated: 12/1/2025, 10:51:13 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxDepth(self, root: Optional[TreeNode]) -> int:
9        self.depth = 0
10
11        def dfs(node, depth):
12            if not node:
13                return
14
15            if depth > self.depth:
16                self.depth = depth
17
18            dfs(node.left, depth + 1)
19            dfs(node.right, depth + 1)
20
21        dfs(root, 1)
22        return self.depth