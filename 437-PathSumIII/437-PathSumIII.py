# Last updated: 7/26/2026, 3:17:09 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
9        self.count = 0
10        freqs = defaultdict(int)
11        freqs[0] = 1
12        
13        def dfs(node, prefix):
14            if not node:
15                return
16
17            prefix += node.val
18            self.count += freqs[prefix - targetSum]
19            freqs[prefix] += 1
20            dfs(node.left, prefix)
21            dfs(node.right, prefix)
22            freqs[prefix] -= 1
23
24        dfs(root, 0)
25        return self.count