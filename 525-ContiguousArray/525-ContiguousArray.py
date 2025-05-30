# Last updated: 5/30/2025, 12:07:50 PM
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        ans = 0
        tracker = {}
        tracker[0] = -1
        counter = 0
        
        for i in range(len(nums)):
            if nums[i] == 0:
                counter += 1
            else:
                counter -= 1
            
            if counter in tracker:
                ans = max(ans, i - tracker[counter])
            else:
                tracker[counter] = i
        
        return ans