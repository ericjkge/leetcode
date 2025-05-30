# Last updated: 5/30/2025, 12:08:04 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return None
        
        dummy = ListNode(0, head) # Add dummy to handle edge cases (e.g. left = 1)

        leftPrev, curr = dummy, head
        for _ in range(left - 1): # Move curr up to left
            leftPrev, curr = curr, curr.next
        
        prev = None
        for _ in range(right - left + 1): # Execute reversal loop
            tempNext = curr.next
            curr.next = prev
            prev, curr = curr, tempNext
        
        leftPrev.next.next = curr # Update pointers
        leftPrev.next = prev
        
        return dummy.next