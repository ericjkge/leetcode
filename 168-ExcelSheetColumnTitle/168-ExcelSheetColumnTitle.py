# Last updated: 5/28/2026, 8:23:00 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
8        if not head:
9            return head
10            
11        n = 0
12        curr = head
13        while curr:
14            curr = curr.next
15            n += 1
16
17        dummy = ListNode(next = head)
18        slow = fast = head
19        
20        for _ in range(k % n):
21            fast = fast.next
22        
23        while fast.next:
24            slow = slow.next
25            fast = fast.next
26        
27        fast.next = dummy.next
28        dummy.next = slow.next
29        slow.next = None
30
31        return dummy.next