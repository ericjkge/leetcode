# Last updated: 12/21/2025, 9:21:50 AM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.next = None
6
7class Solution:
8    def hasCycle(self, head: Optional[ListNode]) -> bool:
9        slow, fast = head, head
10
11        while fast and fast.next:
12            slow = slow.next
13            fast = fast.next.next
14            if slow == fast:
15                return True
16        
17        return False