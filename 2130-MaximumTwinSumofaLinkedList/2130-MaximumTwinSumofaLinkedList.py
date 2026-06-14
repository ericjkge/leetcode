# Last updated: 6/13/2026, 9:43:51 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def pairSum(self, head: Optional[ListNode]) -> int:
8        p = head
9        vals = []
10        while p:
11            vals.append(p.val)
12            p = p.next
13
14        mx = 0
15        left, right = 0, len(vals) - 1
16        while left < right:
17            mx = max(mx, vals[left] + vals[right])
18            left += 1
19            right -= 1
20        
21        return mx