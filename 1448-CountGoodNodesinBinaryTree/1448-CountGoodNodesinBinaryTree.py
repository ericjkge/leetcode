# Last updated: 8/13/2025, 12:38:38 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0

        def dfs(node, largest):
            nonlocal ans
            if not node:
                return

            if node.val < largest:
                pass
            elif node.val > largest:
                largest = node.val
                ans += 1
            else:
                ans += 1

            dfs(node.left, largest)
            dfs(node.right, largest)

        dfs(root, root.val)
        return ans
        1