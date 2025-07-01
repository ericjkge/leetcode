# Last updated: 7/1/2025, 9:26:25 AM
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        ans = []
        carry = 0
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
