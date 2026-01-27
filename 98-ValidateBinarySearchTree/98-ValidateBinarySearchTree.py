# Last updated: 1/27/2026, 11:35:58 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isValidBST(self, root: Optional[TreeNode]) -> bool:
9        tree = []
10
11        def dfs(node):
12            if not node:
13                return
14
15            dfs(node.left)            
16            tree.append(node.val)
17            dfs(node.right)
18        
19        dfs(root)
20        for i in range(len(tree)):
21            if i > 0 and tree[i] <= tree[i - 1]:
22                return False
23        return True