# Last updated: 12/2/2025, 10:05:50 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
9        if not preorder:
10            return None
11
12        root = TreeNode(preorder[0])
13        mid = inorder.index(root.val)
14
15        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
16        root.right = self.buildTree(preorder[mid + 1: ], inorder[mid + 1:])
17
18        return root