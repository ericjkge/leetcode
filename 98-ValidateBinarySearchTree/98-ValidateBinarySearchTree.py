# Last updated: 7/1/2025, 12:56:48 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if node.left:
                dfs(node.left)
            ans.append(node.val)
            if node.right:
                dfs(node.right)
        
        ans = []
        dfs(root)

        for i in range(len(ans)):
            if i > 0 and ans[i] <= ans[i - 1]:
                return False
        
        return True