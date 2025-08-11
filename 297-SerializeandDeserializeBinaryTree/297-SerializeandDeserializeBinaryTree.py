# Last updated: 8/11/2025, 7:53:06 PM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def deserialize(self, data: str) -> TreeNode:
        if not data:
            return None
            
        ls = data.split(",")
        nodes = [None if node == "null" else TreeNode(int(node)) for node in ls]
        
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

        
    def serialize(self, root) -> str:
        if not root:
            return ""
        queue = deque([root])
        
        res = []
        while queue:
            node = queue.popleft()
            if not node:
                res.append("null")
                continue
            res.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)
        
        return ",".join(res)

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))