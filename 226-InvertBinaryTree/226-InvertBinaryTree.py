# Last updated: 4/5/2026, 10:32:11 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
9        if not root:
10            return None
11
12        left = self.invertTree(root.left)
13        right = self.invertTree(root.right)
14
15        root.left, root.right = right, left
16
17        return root