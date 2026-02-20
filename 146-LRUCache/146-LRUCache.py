# Last updated: 2/20/2026, 9:48:12 AM
1class ListNode:
2    def __init__(self, key=None, value=None, nxt=None, prev=None):
3        self.key = key
4        self.value = value
5        self.next = nxt
6        self.prev = prev
7
8class LRUCache:
9
10    def __init__(self, capacity: int):
11        self.capacity = capacity
12        self.cache = defaultdict(ListNode)
13        self.left, self.right = ListNode(), ListNode()
14        self.left.next = self.right
15        self.right.prev = self.left
16
17    def add(self, node):
18        nxt = self.left.next
19        node.next = nxt
20        nxt.prev = node
21        self.left.next = node
22        node.prev = self.left
23
24    def remove(self, node):
25        prev, nxt = node.prev, node.next
26        prev.next, nxt.prev = nxt, prev
27
28    def get(self, key: int) -> int:
29        if key in self.cache:
30            node = self.cache[key]
31            self.remove(node)
32            self.add(node)
33            return self.cache[key].value
34        return -1
35
36    def put(self, key: int, value: int) -> None:
37        if key not in self.cache:
38            self.cache[key] = ListNode(key, value)
39            self.add(self.cache[key])
40
41            if len(self.cache) > self.capacity:
42                node = self.right.prev
43                self.remove(node)
44                del self.cache[node.key]
45        else:
46            node = self.cache[key]
47            node.value = value
48            self.remove(node)
49            self.add(node)
50            
51
52
53
54# Your LRUCache object will be instantiated and called as such:
55# obj = LRUCache(capacity)
56# param_1 = obj.get(key)
57# obj.put(key,value)