# Last updated: 1/25/2026, 8:35:37 AM
1class Solution:
2    def plusOne(self, digits: List[int]) -> List[int]:
3        n = len(digits)
4        carry = 1
5
6        for i in range(n - 1, -1, -1):
7            total = digits[i] + carry
8            if total > 9:
9                carry = 1
10                digits[i] = total % 10
11            else:
12                carry = 0
13                digits[i] = total
14        
15        return [1] + digits if carry else digits 