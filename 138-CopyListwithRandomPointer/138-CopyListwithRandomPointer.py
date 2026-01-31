# Last updated: 1/31/2026, 1:30:01 PM
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
12        mapping = {None:None}
13        curr = head
14
15        while curr:
16            clone = Node(curr.val)
17            mapping[curr] = clone
18            curr = curr.next
19
20        curr = head
21        while curr:
22            clone = mapping[curr]
23            clone.next = mapping[curr.next]
24            clone.random = mapping[curr.random]
25            curr = curr.next
26        
27        return mapping[head]
28