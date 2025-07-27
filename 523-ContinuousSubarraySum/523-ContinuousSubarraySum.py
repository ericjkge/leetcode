# Last updated: 7/27/2025, 10:54:41 PM
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hashmap = {0: -1}
        prefix = 0
        
        for i, num in enumerate(nums):
            prefix += num
            if prefix % k in hashmap:
                if i - hashmap[prefix % k] >= 2:
                    return True
            else:
                hashmap[prefix % k] = i
        
        return False