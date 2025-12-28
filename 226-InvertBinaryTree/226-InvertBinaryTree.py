# Last updated: 12/28/2025, 10:42:04 AM
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
11        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
12        return root
13
14        
15