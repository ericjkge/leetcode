# Last updated: 6/28/2025, 4:15:10 PM
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        ans = []

        while i >= 0 or j >= 0 or carry:
            total = carry
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
            ans.append(str(total % 2))
            carry = total // 2
        
        return "".join(reversed(ans))
