# Last updated: 11/3/2025, 9:41:36 AM
class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans = []

        for i in range(len(nums)):
            if i and nums[i] > nums[i - 1] + 1:
                for j in range(nums[i - 1] + 1, nums[i]):
                    ans.append(j)
        
        return ans