# Last updated: 2/28/2026, 9:53:11 AM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
8        dummy = fast = slow = ListNode(val=0, next=head)
9
10        for _ in range(n):
11            fast = fast.next
12        
13        while fast and fast.next:
14            fast = fast.next
15            slow = slow.next
16        
17        slow.next = slow.next.next
18        return dummy.next