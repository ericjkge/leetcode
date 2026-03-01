# Last updated: 3/1/2026, 12:42:53 PM
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
11        def merge(p1, p2):
12            dummy = curr = ListNode()
13
14            while p1 and p2:
15                if p1.val < p2.val:
16                    curr.next = p1
17                    p1 = p1.next
18                else:
19                    curr.next = p2
20                    p2 = p2.next
21                curr = curr.next
22
23            curr.next = p1 if p1 else p2
24
25            return dummy.next
26
27        while len(lists) > 1:
28            merged = []
29            for i in range(0, len(lists), 2):
30                p1 = lists[i]
31                p2 = lists[i + 1] if i + 1 < len(lists) else None
32                merged.append(merge(p1, p2))
33            lists = merged
34
35        return lists[0]