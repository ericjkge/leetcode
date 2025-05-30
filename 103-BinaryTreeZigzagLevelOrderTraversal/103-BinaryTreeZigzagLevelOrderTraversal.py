# Last updated: 5/30/2025, 12:08:01 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = deque([root])
        ans = []
        counter = 0
        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                print(node.val)
                level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if counter % 2 != 0:
                level.reverse()
            
            print(level)
            ans.append(level)
            counter += 1
        
        return ans
            
        
        
        
        