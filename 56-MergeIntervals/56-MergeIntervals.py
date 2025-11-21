# Last updated: 11/21/2025, 12:44:43 PM
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        prev = -float("inf")
        ans = []
        
        for start, end in intervals:
            if start <= prev:
                ans[-1][1] = max(prev, end)
                prev = ans[-1][1]
            else:
                ans.append([start, end])
                prev = end
        
        return ans

