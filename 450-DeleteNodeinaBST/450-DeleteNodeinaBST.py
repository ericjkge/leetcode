# Last updated: 7/9/2025, 11:34:50 AM
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Node with only one child or no child
            if not root.left:
                return root.right
            if not root.right:
                return root.left

            # Find inorder successor (leftmost in right subtree)
            successor = root.right
            parent = root
            while successor.left:
                parent = successor
                successor = successor.left

            # Replace root with successor node
            if parent != root:
                parent.left = successor.right
                successor.right = root.right
            successor.left = root.left

            return successor

        return root
