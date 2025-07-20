# Last updated: 7/20/2025, 9:30:58 AM
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        counter = Counter(nums)

        def backtrack(path):
            if len(path) == len(nums):
                ans.append(path[:])
                return
            
            for num in counter:
                if counter[num] > 0:
                    path.append(num)
                    counter[num] -= 1
                    backtrack(path)
                    path.pop()
                    counter[num] += 1
        
        backtrack([])
        return ans