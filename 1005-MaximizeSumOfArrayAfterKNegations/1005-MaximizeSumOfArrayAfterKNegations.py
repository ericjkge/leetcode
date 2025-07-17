# Last updated: 7/17/2025, 4:45:29 PM
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        for i in range(len(nums)):
            if k > 0 and nums[i] < 0:
                nums[i] = -nums[i]
                k -= 1
        
        nums.sort()
        if k % 2 == 1:
            nums[0] = -nums[0]
                    
        return sum(nums)
            
# Time: O(nlogn)
# Space: O(1)