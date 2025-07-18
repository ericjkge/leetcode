# Last updated: 7/18/2025, 3:36:23 PM
class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        time = 0
        stack = []
        for index, grow_time in sorted(enumerate(growTime), key=lambda x: -x[1]): # index, time (non-decreasing)
            time += plantTime[index]
            stack.append(grow_time + time) # bloom time

        while stack:
            bloom_time = stack.pop()
            if bloom_time > time:
                time = bloom_time
    
        return time


            