# Last updated: 9/7/2025, 8:18:24 PM
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []

        for start, end in intervals:
            if ans and start <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], end)
            else:
                ans.append([start, end])

        return ans