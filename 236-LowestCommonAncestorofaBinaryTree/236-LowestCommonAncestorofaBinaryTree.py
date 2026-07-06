# Last updated: 7/5/2026, 11:56:23 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.left = None
6#         self.right = None
7
8class Solution:
9    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
10        if root == None:
11            return None
12
13        if root == p or root == q:
14            return root
15        
16        left = self.lowestCommonAncestor(root.left, p, q)
17        right = self.lowestCommonAncestor(root.right, p, q)
18
19        if left and right:
20            return root
21        if left:
22            return left
23        return right