# Last updated: 11/3/2026, 12:36:54 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def searchBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
9        def dfs(node, target):
10            if node is None:
11                return None
12
13            if node.val > target:
14                return dfs(node.left, target)
15            elif node.val < target:
16                return dfs(node.right, target)
17            else:
18                return node
19        
20        return dfs(root, val)
21