# Last updated: 8/20/2025, 11:50:50 PM
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key = lambda x: x[1])
        time = 0
        heap = [] # max heap
        for dur, end in courses:
            if time + dur <= end:
                heapq.heappush(heap, -dur)
                time += dur
            else:
                if heap and -heap[0] > dur:
                    time += dur + heapq.heappop(heap)
                    heapq.heappush(heap, -dur)
        return len(heap)

        # NOTE: DP is MLE
        # courses.sort(key=lambda x:x[1])
        # n = len(courses)

        # @cache
        # def dp(i, t):
        #     if i == n:
        #         return 0
        #     dur, end = courses[i]
        #     skip = dp(i + 1, t)
        #     take = 0
        #     if t + dur <= end:
        #         take = 1 + dp(i + 1, t + dur)
        #     return max(skip, take)

        # return dp(0, 0)