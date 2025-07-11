# Last updated: 7/4/2025, 10:32:41 AM
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        count = Counter(nums)

        total = 0
        for num, freq in count.items():
            if freq == 1:
                total += num
        
        return total