# Last updated: 7/4/2025, 10:31:13 AM
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        hashmap = defaultdict()
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        
        unique = []
        for key in hashmap:
            if hashmap[key] == 1:
                unique.append(key)
        
        return sum(unique) if unique else 0