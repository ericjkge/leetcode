# Last updated: 6/15/2026, 8:50:43 PM
1class Solution:
2    def alienOrder(self, words: List[str]) -> str:
3        chars = set([c for word in words for c in word])
4        graph = defaultdict(list)
5        indegrees = {c: 0 for c in chars}
6
7        for i in range(len(words) - 1):
8            if len(words[i]) > len(words[i + 1]) and words[i].startswith(words[i + 1]):
9                return ""
10
11            for j in range(min(len(words[i]), len(words[i + 1]))):
12                if words[i][j] != words[i + 1][j]:
13                    graph[words[i][j]].append(words[i + 1][j])
14                    indegrees[words[i + 1][j]] += 1
15                    break
16            
17        queue = deque([char for char in indegrees if indegrees[char] == 0])
18        order = [char for char in indegrees if indegrees[char] == 0]
19        while queue:
20            node = queue.popleft()
21            for neighbor in graph[node]:
22                indegrees[neighbor] -= 1
23                if indegrees[neighbor] == 0:
24                    order.append(neighbor)
25                    queue.append(neighbor)
26        
27        if len(order) == len(indegrees):
28            return "".join(order)
29        return ""