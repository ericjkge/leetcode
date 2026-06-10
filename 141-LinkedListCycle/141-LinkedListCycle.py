# Last updated: 6/9/2026, 8:28:37 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.next = None
6
7class Solution:
8    def hasCycle(self, head: Optional[ListNode]) -> bool:
9        slow = fast = head
10
11        while fast and fast.next:
12            fast = fast.next.next
13            slow = slow.next
14
15            if slow == fast:
16                return True
17            
18        return False