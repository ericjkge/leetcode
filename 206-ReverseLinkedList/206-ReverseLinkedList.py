# Last updated: 12/27/2025, 10:26:54 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        prev = None
9        curr = head
10
11        while curr:
12            nxt = curr.next
13            curr.next = prev
14            prev = curr
15            curr = nxt
16        
17        return prev