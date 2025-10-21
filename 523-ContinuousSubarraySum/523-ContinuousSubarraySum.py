# Last updated: 10/21/2025, 2:41:03 PM
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix = 0
        hashmap = {0:-1}

        for i, num in enumerate(nums):
            prefix += num
            if prefix % k in hashmap:
                if (i - hashmap[prefix % k]) >= 2:
                    return True
            else:
                hashmap[prefix % k] = i
        
        return False