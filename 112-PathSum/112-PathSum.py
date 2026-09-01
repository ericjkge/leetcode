# Last updated: 9/1/2026, 11:18:25 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
9        if not root:
10            return False
11
12        def dfs(node, total):
13            if not node:
14                return False
15                
16            total += node.val
17            if not node.left and not node.right:
18                return total == targetSum
19            return dfs(node.left, total) or dfs(node.right, total)
20        
21        return dfs(root, 0)