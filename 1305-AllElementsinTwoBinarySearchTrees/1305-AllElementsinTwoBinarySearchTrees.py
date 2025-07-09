# Last updated: 7/8/2025, 11:24:30 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        def dfs(node, path):
            if not node:
                return

            dfs(node.left, path)
            path.append(node.val)
            dfs(node.right, path)

        tree1 = []
        tree2 = []
        dfs(root1, tree1)
        dfs(root2, tree2)
        
        ans = []
        i = j = 0
        while i < len(tree1) and j < len(tree2):
            if tree1[i] < tree2[j]:
                ans.append(tree1[i])
                i += 1
            else:
                ans.append(tree2[j])
                j += 1
        
        ans.extend(tree1[i:])
        ans.extend(tree2[j:])

        return ans