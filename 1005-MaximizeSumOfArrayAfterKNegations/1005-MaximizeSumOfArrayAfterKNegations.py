# Last updated: 7/17/2025, 4:42:24 PM
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        counter = 0
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = -nums[i]
                counter +=1
            if counter == k:
                break
        
        if counter < k:
            min_val = min(nums)
            if (k - counter) % 2 == 1:
                pos = nums.index(min_val)
                nums[pos] = -nums[pos]
        
        return sum(nums)
            
        # if negative, flip most negative to positive
        # if zero, do remainder on zero
        # else, do remainder on smallest