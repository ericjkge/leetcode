# Last updated: 8/13/2025, 11:50:06 AM
class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        heap = []
        for char, freq in counter.items():
            heapq.heappush(heap, (-freq, char))

        if -heap[0][0] > (len(s) + 1) // 2:
            return ""

        ans = []
        while heap:
            f1, c1 = heapq.heappop(heap)
            if not ans or ans[-1] != c1:
                ans.append(c1)
                f1 += 1
                if f1 < 0:
                    heapq.heappush(heap, (f1, c1))
            else:
                if not heap:
                    return ""
                f2, c2 = heapq.heappop(heap)
                ans.append(c2)
                f2 += 1
                if f2 < 0:
                    heapq.heappush(heap, (f2, c2))
                heapq.heappush(heap, (f1, c1))

        return "".join(ans)