# Last updated: 7/1/2025, 12:16:53 AM
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = [intervals[0]]

        for start, end in intervals:
            if ans[-1][1] >= start:
                ans[-1][1] = max(end, ans[-1][1])
            else:
                ans.append([start, end])
        
        return ans
        