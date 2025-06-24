# Last updated: 6/24/2025, 6:59:13 PM
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        counter = 0

        for num in nums:
            if counter == 0:
                candidate = num
            counter += 1 if num == candidate else -1
            
        return candidate