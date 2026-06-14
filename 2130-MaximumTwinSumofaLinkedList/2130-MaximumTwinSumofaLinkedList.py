# Last updated: 6/13/2026, 9:51:54 PM
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
15        while slow:
16            nxt = slow.next
17            slow.next = prev
18            prev = slow
19            slow = nxt
20
21        p1, p2 = head, prev
22        mx = 0
23
24        while p2:
25            mx = max(mx, p1.val + p2.val)
26            p1 = p1.next
27            p2 = p2.next
28
29        return mx