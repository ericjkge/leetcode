# Last updated: 6/4/2025, 2:16:31 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        seen = {head}
        pointer = head
        while pointer.next:
            pointer = pointer.next
            if pointer in seen:
                return True
            seen.add(pointer)
        
        return False