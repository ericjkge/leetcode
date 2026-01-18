# Last updated: 1/18/2026, 9:26:53 AM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
8        dummy = group_prev = ListNode(0, head)
9
10        while True:
11            kth = group_prev
12            for _ in range(k):
13                kth = kth.next
14                if not kth:
15                    return dummy.next
16
17            group_next = kth.next
18            prev, curr = group_next, group_prev.next
19
20            while curr != group_next:
21                nxt = curr.next
22                curr.next = prev
23                prev = curr
24                curr = nxt
25
26            temp = group_prev.next
27            group_prev.next = prev
28            group_prev = temp