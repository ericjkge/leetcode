# Last updated: 7/27/2025, 12:18:52 AM
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        p1, p2 = len(num1) - 1, len(num2) - 1
        
        ans = []
        carry = 0
        
        while p1 >= 0 or p2 >= 0 or carry:
            x = int(num1[p1]) if p1 >= 0 else 0
            y = int(num2[p2]) if p2 >= 0 else 0
            ans.append(str((x + y + carry) % 10))
            carry = (x + y + carry) // 10
            p1 -= 1
            p2 -= 1
            
        return "".join(reversed(ans))