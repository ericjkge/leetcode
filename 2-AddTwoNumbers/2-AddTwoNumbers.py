# Last updated: 7/21/2025, 11:57:42 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = l1, l2
        dummy = curr = ListNode()
        carry = 0

        while p1 or p2 or carry:
            total = carry
            if p1:
                total += p1.val
                p1 = p1.next
            if p2:
                total += p2.val
                p2 = p2.next
            carry = 0
            if total >= 10:
                carry = 1
                total = total % 10
            curr.next = ListNode(total)
            curr = curr.next

        return dummy.next