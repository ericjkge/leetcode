# Last updated: 7/8/2025, 10:41:38 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(node, total, path):       
            total += node.val
            if not node.left and not node.right:
                if total == targetSum:
                    ans.append(path[:])
                    total -= node.val
                    return
                else:
                    total -= node.val
                    return
            
            if node.left:
                path.append(node.left.val)
                dfs(node.left, total, path)
                path.pop()
            if node.right:
                path.append(node.right.val)
                dfs(node.right, total, path)
                path.pop()

            total -= node.val

        if not root:
            return []

        ans = []
        dfs(root, 0, [root.val])
        return ans