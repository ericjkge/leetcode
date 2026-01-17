# Last updated: 1/17/2026, 12:13:17 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
8        def sort(l1, l2):
9            dummy = curr = ListNode()
10            while l1 and l2:
11                if l1.val < l2.val:
12                    curr.next = l1
13                    l1 = l1.next
14                else:
15                    curr.next = l2
16                    l2 = l2.next
17                curr = curr.next
18            curr.next = l1 if l1 else l2
19            return dummy.next
20
21        while len(lists) > 1:
22            merged = []
23            for i in range(0, len(lists), 2):
24                first = lists[i]
25                second = lists[i + 1] if i + 1 < len(lists) else None
26                merged.append(sort(first, second))
27            lists = merged
28        
29        return lists[0] if lists else None