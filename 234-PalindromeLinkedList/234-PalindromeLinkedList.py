# Last updated: 7/5/2025, 3:51:54 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        
        node = head
        while node:
            stack.append(node.val)
            node = node.next
        
        left = 0
        right = len(stack) - 1
        while left < right:
            if stack[left] != stack[right]:
                return False
            left += 1
            right -= 1
        
        return True