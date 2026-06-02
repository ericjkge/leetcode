# Last updated: 6/1/2026, 10:50:09 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
8        if not lists:
9            return None
10            
11        def merge(l1, l2):
12            res = []
13            dummy = curr = ListNode()
14            while l1 and l2:
15                if l1.val <= l2.val:
16                    curr.next = l1
17                    l1 = l1.next
18                else:
19                    curr.next = l2
20                    l2 = l2.next
21                curr = curr.next
22            curr.next = l1 if l1 else l2
23            return dummy.next
24        
25        merged = []
26        while len(lists) > 1:
27            for i in range(0, len(lists), 2):
28                l1 = lists[i]
29                l2 = lists[i + 1] if i + 1 < len(lists) else None
30                merged.append(merge(l1, l2))
31            lists = merged
32            merged = []
33        
34        return lists[0]