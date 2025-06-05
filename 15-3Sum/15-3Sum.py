# Last updated: 6/5/2025, 4:00:31 PM
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for i, v in enumerate(nums):
            if i != 0 and v == nums[i-1]: # Duplicate value
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[r] + nums[l] > -v:
                    r -= 1
                elif nums[r] + nums[l] < -v:
                    l += 1
                else:
                    ans.append([v, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return ans





