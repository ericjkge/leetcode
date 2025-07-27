# Last updated: 7/27/2025, 9:35:56 PM
class NumArray:


    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix = [self.nums[0]]
        for i in range(1, len(self.nums)):
            self.prefix.append(self.prefix[i - 1] + self.nums[i])

    def sumRange(self, i: int, j: int) -> int:
        if i == 0:
            return self.prefix[j]
        return self.prefix[j] - self.prefix[i - 1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)