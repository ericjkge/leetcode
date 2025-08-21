# Last updated: 8/21/2025, 7:20:31 PM
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        same = defaultdict(list)
        n = len(arr)
        
        for i, val in enumerate(arr):
            same[val].append(i)
        
        queue = deque([0])
        dist = 0
        seen = set([0])
        
        while queue:
            for _ in range(len(queue)):
                index = queue.popleft()
                if index == n - 1:
                    return dist
                
                if index + 1 < n and index + 1 not in seen:
                    seen.add(index + 1)
                    queue.append(index + 1)

                if index - 1 >= 0 and index - 1 not in seen:
                    seen.add(index - 1)
                    queue.append(index - 1)
                
                if same[arr[index]]:
                    for i in same[arr[index]]:
                        if i not in seen:
                            seen.add(i)
                            queue.append(i)
                    same[arr[index]] = []
            dist += 1
            
        return -1