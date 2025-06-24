# Last updated: 6/24/2025, 6:59:58 PM
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = nums[0]
        counter = 1
        for i in range(1, len(nums)):
            if counter == 0:
                candidate = nums[i]
            if nums[i] == candidate:
                counter += 1
            else:
                counter -= 1
        
        return candidate