# Last updated: 7/18/2025, 3:43:17 PM
class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        time = 0
        res = 0
        for index, grow_time in sorted(enumerate(growTime), key=lambda x: -x[1]):
            time += plantTime[index]
            res = max(res, time + grow_time)
        return res


            