# Last updated: 1/31/2026, 1:30:51 PM
1"""
2# Definition for a Node.
3class Node:
4    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
5        self.val = int(x)
6        self.next = next
7        self.random = random
8"""
9
10class Solution:
11    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
12        if not head:
13            return None
14            
15        mapping = {}
16        curr = head
17
18        while curr:
19            clone = Node(curr.val)
20            mapping[curr] = clone
21            curr = curr.next
22
23        curr = head
24        while curr:
25            clone = mapping[curr]
26            if curr.next:
27                clone.next = mapping[curr.next]
28            if curr.random:
29                clone.random = mapping[curr.random]
30            curr = curr.next
31        
32        return mapping[head]
33