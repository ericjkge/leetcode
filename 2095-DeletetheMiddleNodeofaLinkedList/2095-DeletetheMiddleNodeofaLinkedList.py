# Last updated: 7/23/2026, 9:20:14 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        if not head or not head.next:
9            return None
10
11        slow = fast = head
12        prev = None
13
14        while fast and fast.next:
15            fast = fast.next.next
16            prev = slow
17            slow = slow.next
18        
19        prev.next = prev.next.next
20
21        return head