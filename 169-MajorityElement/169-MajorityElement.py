# Last updated: 6/28/2025, 8:27:43 PM
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        curr = nums[0]
        counter = 1
        for i in range(1, len(nums)):
            if counter == 0:
                curr = nums[i]
            if curr == nums[i]:
                counter += 1
            else:
                counter -= 1
        
        return curr