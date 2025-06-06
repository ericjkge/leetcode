# Last updated: 6/6/2025, 3:43:54 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        nodes = []
        for l in lists:
            while l:
                nodes.append(l.val)
                l = l.next
        
        head = curr = ListNode()
        for node in sorted(nodes):
            curr.next = ListNode(node)
            curr = curr.next

        return head.next

