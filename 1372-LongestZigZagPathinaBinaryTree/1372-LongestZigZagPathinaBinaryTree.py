# Last updated: 7/26/2026, 3:35:06 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def longestZigZag(self, root: Optional[TreeNode]) -> int:
9        self.best = 0
10
11        def dfs(node):
12            if not node:
13                return -1, -1
14
15            ll, lr = dfs(node.left)
16            rl, rr = dfs(node.right)
17
18            left, right = 1 + lr, 1 + rl
19
20            self.best = max(self.best, left, right)
21            return left, right
22
23        dfs(root)
24        return self.best