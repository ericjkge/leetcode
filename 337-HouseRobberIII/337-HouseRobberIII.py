# Last updated: 7/6/2026, 12:20:54 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def rob(self, root: Optional[TreeNode]) -> int:
9        @cache
10        def dp(node):
11            if node == None:
12                return 0, 0
13
14            left, right = dp(node.left), dp(node.right)
15
16            return node.val + left[1] + right[1], max(left) + max(right) # rob, skip
17        
18        return max(dp(root))