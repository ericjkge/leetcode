# Last updated: 11/3/2026, 12:09:00 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def longestZigZag(self, root: Optional[TreeNode]) -> int:
9        self.ans = 0
10
11        def dfs(node):
12            if not node:
13                return -1, -1
14            
15            ll, lr = dfs(node.left)
16            rl, rr = dfs(node.right)
17
18            left = 1 + lr
19            right = 1 + rl
20
21            self.ans = max(self.ans, left, right)
22            return left, right
23
24        dfs(root)
25        return self.ans