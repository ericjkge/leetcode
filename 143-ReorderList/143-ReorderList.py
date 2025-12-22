# Last updated: 12/22/2025, 6:53:10 PM
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
13        while fast and fast.next:
14            slow = slow.next
15            fast = fast.next.next
16        
17        prev = None
18        while slow:
19            nxt = slow.next
20            slow.next = prev
21            prev = slow
22            slow = nxt
23        
24        p1 = head
25        p2 = prev
26        
27        while p2.next:
28            n1 = p1.next
29            n2 = p2.next
30            p1.next = p2
31            p2.next = n1
32            p1 = n1
33            p2 = n2
34
35        return head
36        