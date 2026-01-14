# Last updated: 1/14/2026, 11:33:36 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def goodNodes(self, root: TreeNode) -> int:
9        self.counter = 0
10
11        def dfs(node, max_node):
12            if not node:
13                return
14
15            if node.val >= max_node:
16                self.counter += 1
17            
18            max_node = max(max_node, node.val)
19            dfs(node.left, max_node)
20            dfs(node.right, max_node)
21            
22        dfs(root, root.val)
23        return self.counter