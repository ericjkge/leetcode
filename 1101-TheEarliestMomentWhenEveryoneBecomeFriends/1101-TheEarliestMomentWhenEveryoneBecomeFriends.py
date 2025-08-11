# Last updated: 8/11/2025, 3:23:37 PM
class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        group = [i for i in range(n)]
        rank = [1] * n
        self.counter = n
        
        def find(person):
            if group[person] != person:
                group[person] = find(group[person])
            return group[person]
        
        def union(a, b):
            ga, gb = find(a), find(b)
            if ga == gb:
                return
            if rank[ga] < rank[gb]:
                group[ga] = gb
            elif rank[ga] > rank[gb]:
                group[gb] = ga
            else:
                group[ga] = gb
                rank[gb] += 1
            self.counter -= 1
                
        logs.sort()
        for time, a, b in logs:
            union(a, b)
            if self.counter == 1:
                return time
        
        return -1