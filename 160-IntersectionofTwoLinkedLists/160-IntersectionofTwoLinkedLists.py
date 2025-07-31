# Last updated: 7/31/2025, 10:48:24 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        seen = set()
        pa = headA
        pb = headB
        
        while pa or pb:
            if pa:
                if pa in seen:
                    return pa
                seen.add(pa)
                pa = pa.next
            if pb:
                if pb in seen:
                    return pb
                seen.add(pb)
                pb = pb.next
        else:
            return None