# Last updated: 2/27/2026, 8:44:37 AM
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
11        def dfs(node, maximum):
12            if not node:
13                return
14            
15            if node.val >= maximum:
16                self.counter += 1            
17                dfs(node.left, node.val)
18                dfs(node.right, node.val)
19            else:
20                dfs(node.left, maximum)
21                dfs(node.right, maximum)
22    
23        dfs(root, root.val)
24        return self.counter