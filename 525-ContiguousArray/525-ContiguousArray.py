# Last updated: 10/3/2025, 9:49:14 AM
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hashmap = {0:-1}
        prefix = 0
        ans = 0

        for i, num in enumerate(nums):
            if num == 0:
                prefix -= 1
            else:
                prefix += 1
            if prefix in hashmap:
                ans = max(ans, i - hashmap[prefix])
            else:
                hashmap[prefix] = i
        
        return ans