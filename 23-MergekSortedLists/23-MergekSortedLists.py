# Last updated: 7/30/2025, 4:29:29 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Version 1 (time: O(N log k), space: O(k)): heap

        # if not lists:
        #     return None
        
        # heap = []
        # for i, node in enumerate(lists):
        #     if node:
        #         heapq.heappush(heap, (node.val, i, node))

        # dummy = curr = ListNode()
        
        # while heap:
        #     val, i, node = heapq.heappop(heap)
        #     curr.next = node
        #     curr = curr.next
        #     if node.next:
        #         heapq.heappush(heap, (node.next.val, i, node.next))
        
        # return dummy.next

        # Version 2 (time: O(N log k), space: O(1)): merge lists
        def mergeLists(l1, l2):
            dummy = curr = ListNode()
            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            
            curr.next = l1 or l2
            return dummy.next

        if not lists:
            return None
        
        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                if i + 1 < len(lists):
                    mergedLists.append(mergeLists(lists[i], lists[i + 1]))
                else:
                    mergedLists.append(mergeLists(lists[i], None))
            lists = mergedLists
        
        return lists[0]