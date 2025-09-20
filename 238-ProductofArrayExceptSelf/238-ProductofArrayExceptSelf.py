# Last updated: 9/19/2025, 10:52:07 PM
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [nums[0]]
        
        for i in range(1, n):
            prefix.append(prefix[-1] * nums[i])

        suffix = [nums[n - 1]]
        
        for j in range(n - 2, -1, -1):
            suffix.append(suffix[-1] * nums[j])
        suffix.reverse()

        ans = []

        for k in range(n):
            left = prefix[k - 1] if k - 1 >= 0 else 1
            right = suffix[k + 1] if k + 1 < n else 1
            ans.append(left * right)
        
        return ans