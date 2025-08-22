# Last updated: 8/22/2025, 7:15:40 PM
class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        n = len(nums)
        prefix = [0]
        for i in range(n):
            prefix.append(prefix[-1] + nums[i])
        
        def average(i, j): # i, j inclusive
            return (prefix[j + 1] - prefix[i]) / (j - i + 1)

        @cache
        def dp(i, j): # max sum of averages in nums[i:] with j groups
            if j == 1:
                return average(i, n - 1)

            best = 0
            for split in range(i, n - j + 1):
                best = max(best, average(i, split) + dp(split + 1, j - 1))
            return best
                
        return dp(0, k)