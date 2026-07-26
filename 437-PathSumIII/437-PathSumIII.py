# Last updated: 7/26/2026, 3:08:28 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
9        if not root:
10            return 0
11            
12        def dfs(node, total):
13            if not node:
14                return 0
15            
16            if total + node.val == targetSum:
17                return 1 + dfs(node.left, total + node.val) + dfs(node.right, total + node.val)
18            
19            return dfs(node.left, total + node.val) + dfs(node.right, total + node.val)
20
21        return dfs(root, 0) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)