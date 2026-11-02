# Last updated: 11/2/2026, 5:02:19 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.left = None
6#         self.right = None
7
8class Solution:
9    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
10        def dfs(node, p, q):
11            if not node:
12                return None
13                
14            if node == p or node == q:
15                return node
16            
17            left = dfs(node.left, p, q)
18            right = dfs(node.right, p, q)
19            if left and right:
20                return node
21            elif left:
22                return left
23            return right
24        
25        return dfs(root, p, q)