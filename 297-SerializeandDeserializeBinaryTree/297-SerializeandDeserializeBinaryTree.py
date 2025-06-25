# Last updated: 6/25/2025, 11:09:07 AM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        ans = ""
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                ans += str(node.val) + ","
                queue.append(node.left)
                queue.append(node.right)
            else:
                ans += "null,"
        return ans

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        ls = data.split(",")
        root = TreeNode(int(ls[0]))
        queue = deque([root])
        i = 1

        while queue and i < len(ls):
            node = queue.popleft()
            if ls[i] != "null":
                left = TreeNode(int(ls[i]))
                node.left = left
                queue.append(left)
            i += 1
            if i < len(ls) and ls[i] != "null":
                right = TreeNode(int(ls[i]))
                node.right = right
                queue.append(right)
            i += 1

        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))