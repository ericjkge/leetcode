# Last updated: 5/30/2025, 12:07:17 PM
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums

        window = 2 * k + 1
        n = len(nums)
        result = [-1] * n
        if window > n:
            return result

        prefix = [0] * (n + 1) # Add extra 0 in 0th index
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums [i]
        
        for i in range(k, n - k):
            left, right = i - k, i + k
            result[i] = (prefix[right + 1] - prefix[left])//window
        return result