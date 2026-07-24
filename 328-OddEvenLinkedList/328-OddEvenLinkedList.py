# Last updated: 7/23/2026, 9:36:44 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        even_dummy = even = ListNode() 
9        odd_dummy = odd = ListNode
10        cur = head
11        flag = -1
12
13        while cur:
14            if flag == 1:
15                even.next = cur
16                even = even.next
17            else:
18                odd.next = cur
19                odd = odd.next
20            cur = cur.next
21            flag *= -1
22        
23        even.next = None
24        odd.next = even_dummy.next
25        return odd_dummy.next