# Last updated: 7/1/2025, 12:17:45 AM
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []

        for start, end in intervals:
            if ans and start <= ans[-1][1]:
                ans[-1][1] = max(end, ans[-1][1])
            else:
                ans.append([start, end])
        
        return ans
        