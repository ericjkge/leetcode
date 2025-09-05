# Last updated: 9/5/2025, 8:59:23 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a, b = headA, headB

        while a != b:
            if not a:
                a = headB
            else:
                a = a.next
            if not b:
                b = headA
            else:
                b = b.next

        return a if a!= None else None