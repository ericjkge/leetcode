# Last updated: 8/29/2025, 5:12:55 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Version 1 (time: O(N log k), space: O(k)): Heap

        if not lists:
            return None
        
        heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
        
        dummy = curr = ListNode()
        while heap:
            _, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        
        return dummy.next

        # Version 2 (time: O(N log k), space: O(1)): Divide and conquer
        
        # if not lists:
        #     return None

        # def merge(p1, p2):
        #     dummy = curr = ListNode()
        #     while p1 and p2:
        #         if p1.val < p2.val:
        #             curr.next = p1
        #             p1 = p1.next
        #         else:
        #             curr.next = p2
        #             p2 = p2.next
        #         curr = curr.next
        #     curr.next = p1 or p2
        #     return dummy.next
        
        # while len(lists) > 1:
        #     merged = []
        #     i = 0
        #     while i < len(lists):
        #         if i == len(lists) - 1:
        #             merged.append(lists[i])
        #             break
        #         else:
        #             merged.append(merge(lists[i], lists[i + 1]))
        #             i += 2
        #     lists = merged
        
        # return lists[0]