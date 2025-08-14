# Last updated: 8/14/2025, 3:06:48 PM
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)
        ans = 0
        last = neededTime[0]

        for i in range(1, n):
            if colors[i] == colors[i - 1]:
                ans += min(last, neededTime[i])
                last = max(last, neededTime[i])
            else:
                last = neededTime[i]

        return ans