# Last updated: 7/18/2025, 2:33:47 PM
class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        counter = 0
        clips.sort()

        curr_end = next_end = 0

        for start, end in clips:
            if start > curr_end:
                curr_end = next_end
                counter += 1
                if start > curr_end:
                    return -1
            next_end = max(next_end, end)
            if next_end >= time:
                counter += 1
                break
        
        if next_end >= time:
            return counter
        return -1