# Last updated: 12/2/2025, 10:37:17 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isBalanced(self, root: Optional[TreeNode]) -> bool:
9        def dfs(node):
10            if not node:
11                return True, 0
12            
13            lbalanced, lheight = dfs(node.left)
14            rbalanced, rheight = dfs(node.right)
15
16            return (lbalanced and rbalanced and abs(lheight - rheight) <= 1), max(lheight, rheight) + 1
17
18        return dfs(root)[0]