# Last updated: 2/28/2026, 10:00:36 AM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
8        dummy = curr = ListNode()
9        p1, p2 = list1, list2
10
11        while p1 and p2:
12            if p1.val < p2.val:
13                curr.next = p1
14                p1 = p1.next
15            else:
16                curr.next = p2
17                p2 = p2.next
18            curr = curr.next
19        
20        curr.next = p1 if p1 else p2
21        return dummy.next