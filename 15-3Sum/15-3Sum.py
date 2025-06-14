# Last updated: 6/14/2025, 12:50:44 AM
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        print(nums)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] < -nums[i]:
                    left += 1
                elif nums[left] + nums[right] > -nums[i]:
                    right -=1
                else:
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        return ans
