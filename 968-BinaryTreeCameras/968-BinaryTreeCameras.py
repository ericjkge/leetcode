# Last updated: 8/21/2025, 12:34:15 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        @cache
        def dp(node): # min cameras to cover node for 3 conditions
            if not node:
                return 0, 0, float("inf")
            
            left = dp(node.left)
            right = dp(node.right)

            dp0 = left[1] + right[1] # represents parent coverage (no self or child coverage)
            dp1 = min(left[2] + min(right[1:]), min(left[1:]) + right[2])
            dp2 = 1 + min(left) + min(right)

            return dp0, dp1, dp2
        
        return min(dp(root)[1:]) # index 1 onwards since root must be covered (no parent)