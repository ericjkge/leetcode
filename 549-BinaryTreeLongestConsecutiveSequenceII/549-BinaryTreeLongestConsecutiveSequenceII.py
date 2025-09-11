# Last updated: 9/11/2025, 1:19:53 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def dfs(node):
            if not node:
                return 0, 0

            inc = dec = 1
            
            if node.left:
                linc, ldec = dfs(node.left)
                if node.val == node.left.val + 1:
                    dec = ldec + 1
                elif node.val == node.left.val - 1:
                    inc = linc + 1

            if node.right:
                rinc, rdec = dfs(node.right)
                if node.val == node.right.val + 1:
                    dec = max(dec, rdec + 1)
                elif node.val == node.right.val - 1:
                    inc = max(inc, rinc + 1)
            
            self.ans = max(self.ans, inc + dec - 1)
            return inc, dec

        dfs(root)
        return self.ans

