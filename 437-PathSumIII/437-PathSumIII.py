# Last updated: 7/8/2025, 1:29:09 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, total):
            nonlocal counter
            if not node:
                return

            total += node.val
            counter += prefix[total - targetSum]
            prefix[total] += 1
                        
            dfs(node.left, total)
            dfs(node.right, total)

            prefix[total] -= 1
        
        counter = 0
        prefix = defaultdict(int)
        prefix[0] = 1 # this is to account for when total == targetSum right?
        dfs(root, 0)
        return counter