# Last updated: 11/2/2026, 4:42:01 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def leafSimilar(self, root1: TreeNode | None, root2: TreeNode | None) -> bool:
9        leaves1, leaves2 = [], []
10
11        def dfs(node, leaves):
12            if not node:
13                return
14            if not node.left and not node.right:
15                leaves.append(node.val)
16                return
17            
18            dfs(node.left, leaves)
19            dfs(node.right, leaves)
20        
21        dfs(root1, leaves1)
22        dfs(root2, leaves2)
23        return leaves1 == leaves2