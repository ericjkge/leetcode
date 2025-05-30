# Last updated: 5/30/2025, 12:07:38 PM
class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        max_int = -1
        tracker = {}
        
        for num in nums:
            tracker[num] = tracker.get(num, 0) + 1
        
        for num, frequency in tracker.items():
            if frequency == 1:
                if max_int < num:
                    max_int = num
        
        return max_int