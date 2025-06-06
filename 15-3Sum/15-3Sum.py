# Last updated: 6/6/2025, 12:44:39 PM
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for i, v in enumerate(nums):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] > -v:
                    r -= 1
                elif nums[l] + nums[r] < -v:
                    l += 1
                else:
                    ans.append([v, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r: 
                        l += 1
                        
        return ans