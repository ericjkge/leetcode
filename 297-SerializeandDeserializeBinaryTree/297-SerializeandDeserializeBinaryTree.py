# Last updated: 9/10/2025, 10:56:36 AM
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

        res = []
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if not node:
                res.append("null")
                continue
            res.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)

        return ",".join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        
        ls = data.split(",")
        nodes = [TreeNode(int(d)) if d != "null" else None for d in ls]

        slow, fast = 0, 1
        while fast < len(nodes):
            nodes[slow].left = nodes[fast]
            fast += 1
            nodes[slow].right = nodes[fast]
            fast += 1
            slow += 1

            while slow < fast and nodes[slow] == None:
                slow += 1
        
        return nodes[0]


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))