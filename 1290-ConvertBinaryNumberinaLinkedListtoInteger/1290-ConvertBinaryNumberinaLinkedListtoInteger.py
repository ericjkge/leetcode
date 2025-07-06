# Last updated: 7/5/2025, 9:24:45 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        binary = []
        node = head
        while node:
            binary.append(node.val)
            node = node.next
        
        total = power = 0
        for i in range(len(binary) - 1, -1, -1):
            total += 2 ** power if binary[i] == 1 else 0
            power += 1
        
        return total
