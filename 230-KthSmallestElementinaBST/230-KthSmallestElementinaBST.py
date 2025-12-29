# Last updated: 12/29/2025, 8:10:46 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
9        tree = []
10        def dfs(node):
11            if not node:
12                return
13            
14            dfs(node.left)
15            tree.append(node.val)
16            dfs(node.right)
17
18        dfs(root)
19
20        return tree[k - 1]