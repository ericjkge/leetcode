# Last updated: 9/5/2025, 8:59:51 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a, b = headA, headB

        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA
            
        return a if a!= None else None