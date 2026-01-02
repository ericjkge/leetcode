# Last updated: 1/2/2026, 9:24:23 PM
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
16        res = []
17        queue = deque([root])
18        while queue:
19            node = queue.popleft()
20            if not node:
21                res.append("null")
22                continue
23            
24            res.append(str(node.val))
25            queue.append(node.left)
26            queue.append(node.right)
27
28        return ",".join(res)
29
30    def deserialize(self, data):
31        """Decodes your encoded data to tree.
32        
33        :type data: str
34        :rtype: TreeNode
35        """
36        if not data:
37            return []
38
39        data = data.split(",")
40        nodes = [TreeNode(int(d)) if d != "null" else None for d in data]
41        slow, fast = 0, 1
42
43        while fast < len(nodes):
44            nodes[slow].left = nodes[fast]
45            fast += 1
46            nodes[slow].right = nodes[fast]
47            fast += 1
48            slow += 1
49            while slow < len(nodes) and nodes[slow] == None:
50                slow += 1
51        
52        return nodes[0]
53
54
55# Your Codec object will be instantiated and called as such:
56# ser = Codec()
57# deser = Codec()
58# ans = deser.deserialize(ser.serialize(root))