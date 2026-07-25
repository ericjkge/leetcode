# Last updated: 7/24/2026, 10:16:07 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def pairSum(self, head: Optional[ListNode]) -> int:
8        slow = fast = head
9
10        while fast and fast.next:
11            slow = slow.next
12            fast = fast.next.next
13
14        prev = None
15        cur = slow
16
17        while cur:
18            nxt = cur.next
19            cur.next = prev
20            prev = cur
21            cur = nxt
22        
23        p1, p2 = head, prev
24        mx = 0
25
26        while p2:
27            mx = max(mx, p1.val + p2.val)
28            p1 = p1.next
29            p2 = p2.next
30        
31        return mx