# Last updated: 5/30/2025, 12:07:52 PM
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)
        ans = right
        while left <= right:
            mid = (left + right) // 2 # threshold
            
            curr = 0
            
            counter = 1
            for num in nums:
                if curr + num <= mid:
                    curr += num
                else:
                    curr = num
                    counter += 1
                    
            if counter <= k:
                right = mid - 1
                ans = mid
            else:
                left = mid + 1
        
        return ans
                
                