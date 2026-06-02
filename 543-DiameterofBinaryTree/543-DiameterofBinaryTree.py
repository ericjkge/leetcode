# Last updated: 6/1/2026, 10:58:11 PM
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
13                return -1
14            
15            left = dfs(node.left)
16            right = dfs(node.right)
17            self.diameter = max(self.diameter, 2 + left + right)
18            return 1 + max(left, right)
19        
20        dfs(root)
21        return self.diameter