# Last updated: 4/27/2026, 11:37:28 AM
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
16        queue = deque([c for c in indegrees if indegrees[c] == 0])
17        order = []
18
19        while queue:
20            node = queue.popleft()
21            order.append(node)
22            for neighbor in graph[node]:
23                indegrees[neighbor] -= 1
24                if indegrees[neighbor] == 0:
25                    queue.append(neighbor)
26
27        if len(order) == len(chars):
28            return "".join(order)
29        return ""