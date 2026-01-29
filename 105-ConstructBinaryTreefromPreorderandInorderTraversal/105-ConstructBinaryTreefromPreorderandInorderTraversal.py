# Last updated: 1/29/2026, 9:55:44 AM
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
12        node = TreeNode(preorder[0])
13        index = inorder.index(preorder[0])
14
15        node.left = self.buildTree(preorder[1:index + 1], inorder[:index])
16        node.right = self.buildTree(preorder[index + 1:], inorder[index + 1:])
17
18        return node