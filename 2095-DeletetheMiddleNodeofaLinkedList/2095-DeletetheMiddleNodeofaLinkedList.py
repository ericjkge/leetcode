# Last updated: 7/5/2025, 1:44:55 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None

        counter = 0
        dummy = node = head
        while node:
            counter += 1
            node = node.next
        
        mid = counter // 2
        node = dummy
        for _ in range(mid - 1):
            node = node.next
        
        node.next = node.next.next

        return dummy