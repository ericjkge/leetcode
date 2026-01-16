# Last updated: 1/16/2026, 6:53:49 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxPathSum(self, root: Optional[TreeNode]) -> int:
9        self.max = root.val
10        
11        def dfs(node):
12            if not node:
13                return 0
14            
15            left, right = dfs(node.left), dfs(node.right)
16            self.max = max(self.max, node.val + left + right, node.val + left, node.val + right, node.val)
17
18            return max(node.val + left, node.val + right, node.val)
19        
20        dfs(root)
21        return self.max