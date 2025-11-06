# Last updated: 11/6/2025, 10:38:18 AM
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []

        for i in range(n):
            if i and nums[i] == nums[i - 1]:
                continue
            target = -nums[i]
            seen = set()
            left, right = i + 1, n - 1
            while left < right:
                total = nums[left] + nums[right]
                if total == target:                        
                    ans.append([-target, nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif total > target:
                    right -= 1
                else:
                    left += 1

        return ans