# Last updated: 6/28/2025, 10:36:30 AM
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda i: i[0])
        output = [intervals[0]]
        for start, end in intervals:
            prev_end = output[-1][1]
            if start <= prev_end:
                output[-1][1] = max(prev_end, end)
            else:
                output.append([start, end])
        return output
