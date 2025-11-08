# Last updated: 11/7/2025, 7:20:24 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None

        dummy = ListNode(0, head)
        slow = fast = dummy

        for _ in range(n):
            fast = fast.next
                
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next

        return dummy.next
