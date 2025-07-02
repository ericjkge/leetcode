# Last updated: 7/2/2025, 12:30:31 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ans = 0
        counter = 0
        def dfs(node):
            nonlocal ans, counter
            counter += 1
            ans = max(ans, counter)
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
            counter -= 1
        dfs(root)
        return ans
