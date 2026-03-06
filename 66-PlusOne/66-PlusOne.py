# Last updated: 3/6/2026, 11:56:46 AM
1class Solution:
2    def plusOne(self, digits: List[int]) -> List[int]:
3        carry = 1
4
5        for i in range(len(digits) - 1, -1, -1):
6            total = digits[i] + carry
7            digits[i] = total % 10
8            carry = total // 10
9        
10        if carry:
11            digits = [1] + digits
12        
13        return digits