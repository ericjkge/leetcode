# Last updated: 6/14/2026, 10:58:25 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
9        def dfs(node, total):
10            if not node:
11                return False
12            
13            total += node.val
14            if total == targetSum and not node.left and not node.right:
15                return True
16            
17            return dfs(node.left, total) or dfs(node.right, total)
18        
19        return dfs(root, 0)