# Last updated: 2/8/2026, 7:18:50 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.left = None
6#         self.right = None
7
8class Solution:
9    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
10        if not root:
11            return None
12            
13        if root.val > p.val and root.val > q.val:
14            return self.lowestCommonAncestor(root.left, p, q)
15        elif root.val < p.val and root.val < q.val:
16            return self.lowestCommonAncestor(root.right, p, q)
17        return root