# Last updated: 9/26/2025, 9:58:42 AM
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = 0

        for nxt in range(1, len(nums)):
            if nums[nxt] != nums[prev]:
                prev += 1
                nums[prev] = nums[nxt]
        
        return prev + 1