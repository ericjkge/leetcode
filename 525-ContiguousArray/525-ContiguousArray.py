# Last updated: 9/23/2025, 8:45:25 PM
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ans = 0
        prefix = 0
        hashmap = {0:-1}

        for i, num in enumerate(nums):
            prefix += 1 if num == 1 else -1
            if prefix in hashmap:
                ans = max(ans, i - hashmap[prefix])
            else:
                hashmap[prefix] = i

        return ans
    # [0, 1, 2, 3, 4, 5, 4, 3, 2]