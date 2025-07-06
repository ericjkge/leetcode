# Last updated: 7/5/2025, 9:08:14 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow = dummy
        fast = head

        while fast:
            if fast.val == val:
                while fast and fast.val == val:
                    fast = fast.next
                slow.next = fast
            else:
                fast = fast.next
                slow = slow.next
        
        return dummy.next