# Last updated: 7/8/2025, 11:19:57 PM
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

        tree1 = deque()
        tree2 = deque()
        dfs(root1, tree1)
        dfs(root2, tree2)
        
        ans = []
        while tree1 and tree2:
            if tree1[0] < tree2[0]:
                ans.append(tree1.popleft())
            else:
                ans.append(tree2.popleft())
        
        while tree1:
            ans.append(tree1.popleft())
        
        while tree2:
            ans.append(tree2.popleft())

        return ans