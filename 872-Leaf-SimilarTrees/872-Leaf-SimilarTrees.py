# Last updated: 7/24/2026, 10:26:05 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
9        leaves1, leaves2 = [], []
10
11        def dfs(node, lst):
12            if not node:
13                return
14                
15            if not node.left and not node.right:
16                lst.append(node.val)
17                return
18            
19            dfs(node.left, lst)
20            dfs(node.right, lst)
21        
22        dfs(root1, leaves1)
23        dfs(root2, leaves2)
24
25        return leaves1 == leaves2
26