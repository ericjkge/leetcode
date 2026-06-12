# Last updated: 6/11/2026, 10:18:00 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reorderList(self, head: Optional[ListNode]) -> None:
8        """
9        Do not return anything, modify head in-place instead.
10        """
11        slow = fast = head
12
13        while fast.next and fast.next.next:
14            slow = slow.next
15            fast = fast.next.next
16
17        prev = None
18        curr = slow.next
19        slow.next = None
20
21        while curr:
22            nxt = curr.next
23            curr.next = prev
24            prev = curr
25            curr = nxt
26        
27        p1 = head
28        p2 = prev
29        while p2 is not None:
30            n1 = p1.next
31            p1.next = p2
32            n2 = p2.next
33            p2.next = n1
34            p1 = n1
35            p2 = n2