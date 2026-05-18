# Last updated: 5/18/2026, 4:37:08 PM
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
17        queue = deque([c for c in indegrees if indegrees[c] == 0])
18        order = []
19
20        while queue:
21            node = queue.popleft()
22            order.append(node)
23            for neighbor in graph[node]:
24                indegrees[neighbor] -= 1
25                if indegrees[neighbor] == 0:
26                    queue.append(neighbor)
27        
28        if len(order) == len(chars):
29            return "".join(order)
30        return ""