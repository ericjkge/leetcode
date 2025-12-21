# Last updated: 12/21/2025, 9:09:36 AM
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
15        hashmap = {}
16        p1 = head
17
18        while p1:
19            clone = Node(p1.val)
20            hashmap[p1] = clone
21            p1 = p1.next
22        
23        p2 = head
24        
25        while p2:
26            if p2.next:
27                hashmap[p2].next = hashmap[p2.next]
28            if p2.random:
29                hashmap[p2].random = hashmap[p2.random]
30            p2 = p2.next
31        
32        return hashmap[head]
33
34