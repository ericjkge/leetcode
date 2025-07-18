# Last updated: 7/18/2025, 4:26:18 PM
class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        intervals = []
        for mid, rad in enumerate(ranges):
            intervals.append([mid - rad, mid + rad])
        
        intervals.sort()
        curr_end = next_end = counter = 0

        for start, end in intervals:
            if start > curr_end:
                curr_end = next_end
                counter += 1
                if start > curr_end:
                    return -1
            next_end = max(next_end, end)
            if next_end >= n:
                counter += 1
                break
        
        if next_end >= n:
            return counter
        return -1