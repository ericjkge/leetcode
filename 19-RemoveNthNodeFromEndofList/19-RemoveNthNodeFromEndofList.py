# Last updated: 1/15/2026, 1:00:35 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
8        dummy = slow = fast = ListNode(0, head)
9
10        for _ in range(n):
11            fast = fast.next
12        
13        while fast and fast.next:
14            slow = slow.next
15            fast = fast.next
16        
17        slow.next = slow.next.next
18
19        return dummy.next