# Last updated: 7/5/2025, 8:12:37 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        before = dummy
        curr = head
        group_size = 1

        while curr:

            # Step 1: Find actual length
            group_tail = curr
            count = 1
            while count < group_size and group_tail.next:
                group_tail = group_tail.next
                count += 1
            
            next_head = group_tail.next
                
            # Step 2: Reverse the current group
            if count % 2 == 0:
                prev = None
                node = curr
                for _ in range(count):
                    nxt = node.next
                    node.next = prev
                    prev = node
                    node = nxt
                before.next = prev
                curr.next = next_head
                before = curr                
            else:
                before = group_tail
            
            curr = next_head
            group_size += 1

        return dummy.next