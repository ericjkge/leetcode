# Last updated: 8/11/2025, 2:55:42 PM
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        rank = [i for i in range(26)]

            
        def find(node):
            if rank[node] != node:
                rank[node] = find(rank[node])
            return rank[node]

            
        def union(a, b):
            ra, rb = find(a), find(b)
            if ra != rb:
                rank[ra] = rb # No union by rank because tree height is at most 26

        for equation in equations:
            if equation[1] == "=":
                union(ord(equation[0]) - ord("a"), ord(equation[3]) - ord("a"))
        
        for equation in equations:
            if equation[1] == "!":
                if find(ord(equation[0]) - ord("a")) == find(ord(equation[3]) - ord("a")):
                    return False
        
        return True
