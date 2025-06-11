# Last updated: 6/11/2025, 12:26:03 AM
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            
            # Left sorted portion
            if nums[l] <= nums[mid]:
                if nums[l] > target or nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1

            # Right sorted portion
            else:
                if nums[r] < target or nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
        
        return -1