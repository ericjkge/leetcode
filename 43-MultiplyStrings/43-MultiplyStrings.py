# Last updated: 11/17/2025, 9:49:50 AM
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        m, n = len(num1), len(num2)
        res = [0] * (m + n)

        for j in range(n - 1, -1, -1):
            for i in range(m - 1, -1, -1):
                prod = (ord(num1[i]) - 48) * (ord(num2[j]) - 48)
                s = prod + res[i + j + 1]

                res[i + j + 1] = s % 10
                res[i + j] += s // 10 # Store carry for next prod
        
        i = 0
        while i < len(res) and res[i] == 0:
            i += 1

        return "".join(str(x) for x in res[i:])
        




        return ans