# Last updated: 5/30/2025, 12:07:31 PM
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def check(divisor):
            return sum(ceil(num/divisor) for num in nums) <= threshold

        left = 1
        right = 10 ** 6
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left