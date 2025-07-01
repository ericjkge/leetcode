# Last updated: 6/30/2025, 9:43:06 PM
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = defaultdict(list)
        hashmap = {}

        for account in accounts:
            name = account[0]
            emails = account[1:]
            for email in emails:
                hashmap[email] = name
            for i in range(len(emails)): # Creates self loop on 0
                graph[emails[0]].append(emails[i])
                graph[emails[i]].append(emails[0])
        
        def dfs(email, component):
            seen.add(email)
            component.append(email)
            for neighbor in graph[email]:
                if neighbor not in seen:
                    dfs(neighbor, component)
        
        seen = set()
        ans = []
        for email in graph:
            component = []
            if email not in seen:
                dfs(email, component)
                ans.append([hashmap[email]] + sorted(component))
        
        return ans
                