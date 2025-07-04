# Last updated: 7/3/2025, 11:40:34 PM
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefix = [0]
        for i in range(1, len(gain) + 1):
            prefix.append(prefix[i - 1] + gain[i - 1])
        
        return max(prefix)