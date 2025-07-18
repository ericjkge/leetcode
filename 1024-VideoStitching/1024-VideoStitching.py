# Last updated: 7/18/2025, 2:30:36 PM
class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        counter = 1
        clips.sort()

        curr_end = zero_counter = 0

        while zero_counter < len(clips) and clips[zero_counter][0] == 0:
            curr_end = max(curr_end, clips[zero_counter][1])
            zero_counter += 1

        next_end = curr_end

        if curr_end >= time: # Edge case for initial full clip
            return counter

        for start, end in clips:
            if start <= curr_end:
                next_end = max(next_end, end)
            else:
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