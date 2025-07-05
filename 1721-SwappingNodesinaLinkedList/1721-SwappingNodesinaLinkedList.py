# Last updated: 7/5/2025, 3:29:38 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        initial = slow = fast = head
        fast = fast.next

        for _ in range(k - 1):
            initial = initial.next
            fast = fast.next
        
        while fast:
            slow = slow.next
            fast = fast.next
        
        temp = initial.val
        initial.val = slow.val
        slow.val = temp

        return head