# Last updated: 12/28/2025, 10:26:48 AM
1class Solution:
2    def containsDuplicate(self, nums: List[int]) -> bool:
3        counts = Counter(nums)
4        return any(val > 1 for val in counts.values())