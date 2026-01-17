# Last updated: 1/17/2026, 11:40:37 AM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
8        dummy = curr = ListNode()
9
10        while list1 or list2:
11            if not list2 or list1 and list1.val < list2.val:
12                curr.next = list1
13                list1 = list1.next
14            else:
15                curr.next = list2
16                list2 = list2.next
17            curr = curr.next
18        
19        return dummy.next