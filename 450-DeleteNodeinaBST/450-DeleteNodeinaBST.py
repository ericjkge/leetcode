# Last updated: 11/4/2026, 7:53:41 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def deleteNode(self, root: TreeNode | None, key: int) -> TreeNode | None:
9        if not root:
10            return None
11
12        if root.val > key:
13            root.left = self.deleteNode(root.left, key)
14            return root
15        elif root.val < key:
16            root.right = self.deleteNode(root.right, key)
17            return root
18        else:
19            if not root.left:
20                return root.right
21            elif not root.right:
22                return root.left
23            else:
24                left = root.left
25                right = root.right
26                node = right
27                while node.left:
28                    node = node.left
29                node.left = left
30                return right