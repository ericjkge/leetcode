# Last updated: 8/9/2026, 11:53:17 AM
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
13            if not node.left and not node.right:
14                if total + node.val == targetSum:
15                    return True
16                return False
17            
18            total += node.val
19            if node.left and dfs(node.left, total):
20                return True
21            
22            if node.right and dfs(node.right, total):
23                return True
24
25            return False
26        
27        return dfs(root, 0)