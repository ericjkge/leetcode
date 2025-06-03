# Last updated: 6/3/2025, 2:29:00 PM
class Solution(object):
    def twoSum(self, nums, target):
        values = {}
        for i in range(len(nums)):
            values[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in values and values[complement] != i:
                return [i, values.get(complement)]
        return []

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        