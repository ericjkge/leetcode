# Last updated: 9/17/2025, 11:45:11 PM
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hashmap = {0:-1}
        prefix = 0

        for i, num in enumerate(nums):
            prefix += num
            if prefix % k in hashmap:
                if i - hashmap[prefix % k] >= 2:
                    return True
            else:
                hashmap[prefix % k] = i

        return False