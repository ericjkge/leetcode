# Last updated: 7/4/2025, 1:07:55 AM
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix = [nums[0]]
        for i in range(1, len(nums)):
            self.prefix.append(self.prefix[i - 1] + self.nums[i])

    def sumRange(self, left: int, right: int) -> int:
        left = self.prefix[left - 1] if left > 0 else 0
        right = self.prefix[right]
        return right - left

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)