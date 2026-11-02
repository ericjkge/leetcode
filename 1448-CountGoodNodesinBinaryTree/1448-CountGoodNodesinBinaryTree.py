# Last updated: 11/2/2026, 4:51:19 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def goodNodes(self, root: TreeNode) -> int:
9        self.count = 0
10
11        def dfs(node, largest):
12            if node is None:
13                return
14
15            if node.val >= largest:
16                largest = node.val
17                self.count += 1
18            
19            dfs(node.left, largest)
20            dfs(node.right, largest)
21        
22        dfs(root, root.val)
23        return self.count
24            
25