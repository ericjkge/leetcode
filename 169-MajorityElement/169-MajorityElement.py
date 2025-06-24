# Last updated: 6/24/2025, 6:29:53 PM
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        threshold = len(nums) // 2
        mapping = defaultdict()

        for num in nums:
            if mapping.get(num) == threshold:
                return num
            mapping[num] = mapping.get(num, 0) + 1