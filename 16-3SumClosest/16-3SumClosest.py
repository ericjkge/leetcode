# Last updated: 7/25/2025, 11:06:45 PM
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff = float("inf")
        ans = None
        
        for i in range(len(nums) - 2):
            goal = target - nums[i]
            p1, p2 = i + 1, len(nums) - 1
            while p1 < p2: 
                if nums[p1] + nums[p2] == goal:
                    return target
                
                total = nums[i] + nums[p1] + nums[p2]
                if abs(target - total) < diff:
                    diff = abs(target - total)
                    ans = total
                    
                if nums[p1] + nums[p2] < goal:
                    p1 += 1
                else:
                    p2 -= 1

        return ans