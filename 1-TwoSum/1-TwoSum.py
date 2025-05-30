# Last updated: 5/30/2025, 12:08:36 PM
class Solution(object):
    def twoSum(self, nums, target):
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]
        return []

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        