# Last updated: 1/25/2026, 8:16:06 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
9        def isSameTree(n1, n2):
10            if not n1 and not n2:
11                return True
12            elif not n1 or not n2:
13                return False
14            
15            if n1.val != n2.val:
16                return False
17            
18            return isSameTree(n1.left, n2.left) and isSameTree(n1.right, n2.right)
19
20        if not root:
21            return False
22            
23        return isSameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)