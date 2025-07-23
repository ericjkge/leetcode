# Last updated: 7/24/2025, 12:19:15 AM
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:

        @cache
        def dp(i): # Max score difference in stoneValue[i:]
            if i >= len(stoneValue):
                return 0
            
            result = -float("inf")
            curr = 0

            for j in range(1, 4):
                if i + j - 1 < len(stoneValue):
                    curr += stoneValue[i + j - 1]
                    result = max(result, curr - dp(i + j))

            return result

        res = dp(0)

        if res > 0:
            return "Alice"
        elif res < 0:
            return "Bob"
        return "Tie"