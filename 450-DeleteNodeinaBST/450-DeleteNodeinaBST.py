# Last updated: 7/9/2025, 12:09:48 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            
            node = root.right
            parent = root
            while node.left:
                parent = node
                node = node.left
            
            if parent != root:
                parent.left = node.right
                node.right = root.right

            node.left = root.left
            
            return node
        
        return root