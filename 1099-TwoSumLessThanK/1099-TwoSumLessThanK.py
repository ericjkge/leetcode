# Last updated: 7/25/2025, 11:36:49 PM
class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        ans = -1
        nums.sort()
        
        p1, p2 = 0, len(nums) - 1

        while p1 < p2:
            total = nums[p1] + nums[p2]
            if ans < total < k:
                ans = total

            if total >= k:
                p2 -= 1
            else:
                p1 += 1
            
        return ans