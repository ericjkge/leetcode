# Last updated: 6/5/2025, 2:35:38 PM
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        mapping = defaultdict()
        for i in range(len(nums)):
            mapping[nums[i]] = i
        
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in mapping and mapping[complement] != i:
                return i, mapping[complement]
        return -1
        