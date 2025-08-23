# Last updated: 8/24/2025, 12:25:43 AM
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        hashmap = defaultdict(str)
        graph = defaultdict(list)

        for account in accounts:
            name = account[0]
            emails = account[1:]
            for email in emails:
                hashmap[email] = name
            for i in range(len(emails)):
                graph[emails[0]].append(emails[i])
                graph[emails[i]].append(emails[0])
        
        seen = set()
        def dfs(email):
            seen.add(email)
            component.append(email)
            for neighbor in graph[email]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor)

        ans = []
        for email in hashmap:
            if email not in seen:
                seen.add(email)
                component = []
                dfs(email)
                ans.append([hashmap[email]] + sorted(component))

        return ans