# Last updated: 11/6/2025, 9:52:00 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.ans = 0

        def dfs(node, m):
            if not node:
                return None

            if node.val >= m:
                self.ans += 1

            m = max(m, node.val)
            dfs(node.left, m)
            dfs(node.right, m)

        dfs(root, -float("inf"))
        return self.ans