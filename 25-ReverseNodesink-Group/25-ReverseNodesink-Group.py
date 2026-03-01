# Last updated: 3/1/2026, 1:20:40 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
8        dummy = group_prev = ListNode(0, head)
9        group_next = head
10
11        while True:
12            for _ in range(k):
13                if not group_next:
14                    return dummy.next
15                group_next = group_next.next            
16            
17            curr = group_prev.next
18            prev = group_prev
19            while curr != group_next:
20                nxt = curr.next
21                curr.next = prev
22                prev = curr
23                curr = nxt
24            
25            temp = group_prev.next
26            temp.next = group_next
27            group_prev.next = prev
28            group_prev = temp 