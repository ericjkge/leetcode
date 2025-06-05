# Last updated: 6/5/2025, 3:26:08 PM
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        mapping = defaultdict()
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in mapping:
                return i, mapping[complement]
            mapping[nums[i]] = i

        return -1
        