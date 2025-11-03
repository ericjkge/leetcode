# Last updated: 11/2/2025, 9:12:41 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        ans = []
        def dfs(node):
            ans.append(str(node.val))
            if node.left and node.right:
                ans.append("(")
                dfs(node.left)
                ans.append(")(")
                dfs(node.right)
                ans.append(")")
            elif node.left:
                ans.append("(")
                dfs(node.left)
                ans.append(")")
            elif node.right:
                ans.append("()")
                ans.append("(")
                dfs(node.right)
                ans.append(")")

        dfs(root)
        return "".join(ans)