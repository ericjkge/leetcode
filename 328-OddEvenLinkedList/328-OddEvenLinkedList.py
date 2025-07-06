# Last updated: 7/5/2025, 10:10:36 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        odd = head
        even = head.next
        dummy = even

        while even and even.next:
            next_even = even.next.next
            next_odd = odd.next.next

            even.next = next_even
            even = even.next

            odd.next = next_odd
            odd = odd.next
        
        odd.next = dummy

        return head
        