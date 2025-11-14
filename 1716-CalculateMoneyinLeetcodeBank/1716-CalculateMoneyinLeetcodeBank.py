# Last updated: 11/14/2025, 2:46:55 PM
class Solution:
    def totalMoney(self, n: int) -> int:
        ans = 0
        week = 1

        for day in range(n):
            ans += week + (day % 7)
            if day % 7 == 6:
                week += 1

        return ans