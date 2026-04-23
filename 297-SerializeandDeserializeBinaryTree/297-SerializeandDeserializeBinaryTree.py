# Last updated: 4/23/2026, 9:51:18 AM
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
16        if not root:
17            return ""
18
19        serial = []
20        queue = deque([root])
21        while queue:
22            node = queue.popleft()
23            if not node:
24                serial.append("null")
25                continue
26
27            serial.append(str(node.val))
28            queue.append(node.left)
29            queue.append(node.right)
30        
31        return ",".join(serial)
32
33    def deserialize(self, data):
34        """Decodes your encoded data to tree.
35        
36        :type data: str
37        :rtype: TreeNode
38        """
39        if not data:
40            return None
41
42        lst = data.split(",")
43        tree = [TreeNode(val) if val != "null" else None for val in lst]
44
45        p1, p2 = 0, 1
46        while p2 < len(tree):
47            tree[p1].left = tree[p2]
48            p2 += 1
49            tree[p1].right = tree[p2]
50            p2 += 1
51            p1 += 1
52            while p1 < len(tree) and tree[p1] == None:
53                p1 += 1
54        
55        return tree[0]
56
57# Your Codec object will be instantiated and called as such:
58# ser = Codec()
59# deser = Codec()
60# ans = deser.deserialize(ser.serialize(root))