# Last updated: 1/14/2026, 12:14:12 AM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
8        carry = 0
9        curr = dummy = ListNode()
10
11        while l1 or l2 or carry:
12            total = carry
13            if l1:
14                total += l1.val
15                l1 = l1.next
16            if l2:
17                total += l2.val
18                l2 = l2.next
19            if total >= 10:
20                carry = 1
21                total -= 10
22            else:
23                carry = 0
24            curr.next = ListNode(total)
25            curr = curr.next
26        
27        return dummy.next