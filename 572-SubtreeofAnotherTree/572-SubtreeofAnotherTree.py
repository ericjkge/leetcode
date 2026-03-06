# Last updated: 3/6/2026, 11:45:12 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
9        if not root:
10            return False
11
12        def isSameTree(n1, n2):
13            if not n1 and not n2:
14                return True
15
16            if not n1 or not n2:
17                return False
18            
19            if n1.val == n2.val: 
20                return isSameTree(n1.left, n2.left) and isSameTree(n1.right, n2.right)
21            return False
22        
23        return isSameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)