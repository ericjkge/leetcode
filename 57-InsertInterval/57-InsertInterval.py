# Last updated: 6/8/2025, 9:16:41 PM
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        print(intervals)
        ans = []
        
        for start, end in intervals:
            if ans and start <= ans[-1][1]:
                ans[-1][1] = max(end, ans[-1][1])
            else:
                ans.append([start, end])
        
        return ans
                