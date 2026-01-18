# Last updated: 1/18/2026, 9:38:28 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
9        self.diameter = 0
10
11        def dfs(node):
12            if not node:
13                return 0
14
15            left = dfs(node.left)
16            right = dfs(node.right)
17
18            self.diameter = max(self.diameter, left + right)
19
20            return 1 + max(left, right)
21        
22        dfs(root)
23        return self.diameter