# Last updated: 7/8/2025, 10:47:14 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(node, total, path):      
            if not node:
                return

            total += node.val
            path.append(node.val)
            if not node.left and not node.right and total == targetSum:
                ans.append(path[:])
            else:
                dfs(node.left, total, path)
                dfs(node.right, total, path)
            path.pop()

        ans = []
        dfs(root, 0, [])
        return ans