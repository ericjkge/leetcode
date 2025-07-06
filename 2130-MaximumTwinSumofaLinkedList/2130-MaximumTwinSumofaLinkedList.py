# Last updated: 7/5/2025, 8:57:11 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        max_sum = 0

        # 1. Find mid
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Reverse second half
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        
        # 3. Scan twin sums
        node = head
        while prev:
            max_sum = max(max_sum, prev.val + node.val)
            prev = prev.next
            node = node.next
        
        return max_sum
