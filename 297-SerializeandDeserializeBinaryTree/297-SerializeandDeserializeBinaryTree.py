# Last updated: 2/14/2026, 6:22:12 PM
1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, x):
4#         self.val = x
5#         self.left = None
6#         self.right = None
7
8class Codec:
9
10    def serialize(self, root):
11        """Encodes a tree to a single string.
12        
13        :type root: TreeNode
14        :rtype: str
15        """
16        serialization = []
17
18        queue = deque([root])
19        while queue:
20            node = queue.popleft()
21
22            if not node:
23                serialization.append("null")
24                continue
25
26            serialization.append(str(node.val))
27            queue.append(node.left)
28            queue.append(node.right)
29        
30        return ",".join(serialization)
31
32    def deserialize(self, data):
33        """Decodes your encoded data to tree.
34        
35        :type data: str
36        :rtype: TreeNode
37        """
38        vals = data.split(",")
39        nodes = [TreeNode(int(v)) if v != "null" else None for v in vals]
40        slow = 0
41        fast = 1
42
43        while fast < len(nodes):
44            nodes[slow].left = nodes[fast]
45            fast += 1
46            nodes[slow].right = nodes[fast]
47            slow += 1
48            while slow < fast and nodes[slow] is None:
49                slow += 1
50            fast += 1
51
52        return nodes[0]
53
54# Your Codec object will be instantiated and called as such:
55# ser = Codec()
56# deser = Codec()
57# ans = deser.deserialize(ser.serialize(root))