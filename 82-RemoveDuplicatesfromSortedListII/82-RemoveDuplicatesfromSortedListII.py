# Last updated: 7/5/2025, 3:03:55 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        dummy = ListNode(0, head)
        slow = dummy
        fast = head

        while fast:
            if fast.next and fast.val == fast.next.val:
                dup_val = fast.val
                while fast and fast.val == dup_val:
                    fast = fast.next
                slow.next = fast
            else:
                slow = fast
                fast = fast.next


        return dummy.next

