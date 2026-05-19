# Last updated: 5/19/2026, 9:22:39 AM
1class Solution:
2    def alienOrder(self, words: List[str]) -> str:
3        chars = set([c for word in words for c in word])
4        graph = defaultdict(list)
5        indegrees = {c: 0 for c in chars}
6
7        for i in range(len(words) - 1):
8            if len(words[i]) > len(words[i + 1]) and words[i].startswith(words[i + 1]):
9                return ""
10            for j in range(min(len(words[i]), len(words[i + 1]))):
11                if words[i][j] != words[i + 1][j]:
12                    graph[words[i][j]].append(words[i + 1][j])
13                    indegrees[words[i + 1][j]] += 1
14                    break
15
16        queue = deque([c for c in chars if indegrees[c] == 0])
17        order = []
18        while queue:
19            node = queue.popleft()
20            order.append(node)
21            for neighbor in graph[node]:
22                indegrees[neighbor] -= 1
23                if indegrees[neighbor] == 0:
24                    queue.append(neighbor)
25        
26        if len(order) != len(chars):
27            return ""
28        return "".join(order)