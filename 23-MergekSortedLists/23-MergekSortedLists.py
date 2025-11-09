# Last updated: 11/8/2025, 9:03:36 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
            
        def mergeLists(list1, list2):
            dummy = curr = ListNode()

            while list1 and list2:
                if list1.val < list2.val:
                    curr.next = list1
                    list1 = list1.next
                else:
                    curr.next = list2
                    list2 = list2.next
                curr = curr.next
            
            curr.next = list1 if list1 else list2

            return dummy.next
        
        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                if i + 1 < len(lists):
                    merged.append(mergeLists(lists[i], lists[i + 1]))
                else:
                    merged.append(lists[i])
            lists = merged
        
        return lists[0]