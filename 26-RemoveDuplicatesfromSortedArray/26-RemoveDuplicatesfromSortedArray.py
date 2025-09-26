# Last updated: 9/26/2025, 9:55:44 AM
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        prev = 0

        for nxt in range(n):
            if nxt and nums[nxt] == nums[nxt - 1]:
                continue
            else:
                nums[prev] = nums[nxt]
                prev += 1
        
        return prev