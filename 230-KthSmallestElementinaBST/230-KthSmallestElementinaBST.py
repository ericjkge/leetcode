# Last updated: 2/8/2026, 4:55:09 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
9        values = []
10
11        def dfs(node):
12            if not node:
13                return
14            
15            dfs(node.left)
16            values.append(node.val)
17            dfs(node.right)
18        
19        dfs(root)
20        return values[k - 1]